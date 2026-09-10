"""FastAPI application factory and command-line runner."""

from __future__ import annotations

from contextlib import asynccontextmanager
import os
from pathlib import Path
from typing import List, Optional, Union

from fastapi import FastAPI, File, Form, HTTPException, Request, Response, UploadFile, status
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from ..query_models import (
    CountsQueryResponse,
    CurrentStateQueryResponse,
    IsConnectedQueryResponse,
    StringQueryResponse,
    parse_query_response,
)
from .broker_service import BrokerAlreadyExistsError, BrokerNotFoundError, BrokerService
from .models import (
    ActionResponse,
    BrokerCreateRequest,
    BrokerListResponse,
    BrokerSummary,
    CommandRequest,
    HealthResponse,
    QueryRequest,
    QueryResponse,
    TimeBarrierRequest,
    DatabaseInfo,
    LogResponse,
    RunnerFederateEdit,
    RunnerFileResponse,
    RunnerFolderRequest,
    RunnerNameRequest,
    RunnerPathRequest,
    RunnerRunResponse,
    RunnerStatusRequest,
    RunnerStatusResponse,
    UploadResponse,
)
from .observer_service import ObserverDatabaseError, ObserverDatabaseService
from .profile_service import ProfileError, ProfileService
from .runner_service import RunnerFileError, RunnerService


def create_app(
    service: Optional[BrokerService] = None,
    runner_service: Optional[RunnerService] = None,
    observer_service: Optional[ObserverDatabaseService] = None,
    profile_service: Optional[ProfileService] = None,
    server_url: Optional[str] = None,
) -> FastAPI:
    """Create the HELICS web API application.

    ``service`` is injectable so callers can test or embed the application
    without sharing global broker state.  ``server_url`` configures the API
    base propagated to runner subprocesses; it defaults to
    ``HELICS_CLI_SERVER_API`` or the local FastAPI address.
    """
    broker_service = service or BrokerService()
    runner = runner_service or RunnerService(server_url=server_url)
    observer = observer_service or ObserverDatabaseService()
    profiler = profile_service or ProfileService()

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        yield
        await run_in_threadpool(broker_service.shutdown)
        await run_in_threadpool(runner.shutdown)

    app = FastAPI(
        title="HELICS Server API",
        version="1.0.0",
        description="Manage HELICS brokers, federations, runs, observer databases, and profiles.",
        lifespan=lifespan,
    )
    # Expose service instances for embedding applications and diagnostics;
    # routes still use the closed-over, lock-protected objects above.
    app.state.broker_service = broker_service
    app.state.runner_service = runner
    app.state.observer_service = observer
    app.state.profile_service = profiler
    cors_origins = [
        origin.strip()
        for origin in os.environ.get(
            "HELICS_WEB_CORS_ORIGINS",
            "http://localhost:5173,http://127.0.0.1:5173",
        ).split(",")
        if origin.strip()
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
    templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "templates"))

    def not_found(error: BrokerNotFoundError) -> HTTPException:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Broker '{error}' not found"
        )

    @app.get("/api/v1/health", response_model=HealthResponse, tags=["system"])
    async def health() -> HealthResponse:
        return HealthResponse()

    # Jinja2/HTMX broker page ------------------------------------------
    async def broker_page_context(request: Request, error: Optional[str] = None) -> dict:
        return {
            "request": request,
            "brokers": await run_in_threadpool(broker_service.list),
            "error": error,
        }

    @app.get("/broker", response_class=HTMLResponse, include_in_schema=False)
    async def broker_page(request: Request) -> HTMLResponse:
        return templates.TemplateResponse(
            request=request,
            name="broker.html",
            context=await broker_page_context(request),
        )

    @app.get("/broker/fragment", response_class=HTMLResponse, include_in_schema=False)
    async def broker_fragment(request: Request) -> HTMLResponse:
        return templates.TemplateResponse(
            request=request,
            name="_broker_list.html",
            context=await broker_page_context(request),
        )

    def optional_form_int(value: str, field: str) -> Optional[int]:
        if not value.strip():
            return None
        try:
            return int(value)
        except ValueError as error:
            raise ValueError(f"{field} must be an integer") from error

    def optional_form_names(value: str) -> List[str]:
        """Parse the comma-separated federate names used by the HTML form."""
        if not value.strip():
            return []
        return [name.strip() for name in value.split(",")]

    async def broker_action_response(request: Request, error: Optional[str] = None) -> HTMLResponse:
        return templates.TemplateResponse(
            request=request,
            name="_broker_list.html",
            context=await broker_page_context(request, error),
        )

    @app.post("/broker/actions/create", response_class=HTMLResponse, include_in_schema=False)
    async def broker_page_create(
        request: Request,
        name: str = Form(...),
        core_type: str = Form("zmq"),
        num_federates: str = Form(""),
        local_federates: str = Form(""),
        local_subbrokers: str = Form(""),
        required_federates: str = Form(""),
        port: str = Form(""),
        log_level: str = Form(""),
    ) -> HTMLResponse:
        try:
            broker_request = BrokerCreateRequest(
                name=name,
                core_type=core_type,
                num_federates=optional_form_int(num_federates, "num_federates"),
                local_federates=optional_form_int(local_federates, "local_federates"),
                local_subbrokers=optional_form_int(local_subbrokers, "local_subbrokers"),
                required_federates=optional_form_names(required_federates),
                port=optional_form_int(port, "port"),
                log_level=log_level or None,
            )
            await run_in_threadpool(broker_service.create, broker_request)
        except Exception as error:
            return await broker_action_response(request, str(error))
        return await broker_action_response(request)

    @app.post("/broker/actions/delete/{name}", response_class=HTMLResponse, include_in_schema=False)
    async def broker_page_delete(request: Request, name: str) -> HTMLResponse:
        try:
            await run_in_threadpool(broker_service.delete, name)
        except BrokerNotFoundError:
            return await broker_action_response(request, f"Broker '{name}' not found")
        except Exception as error:
            return await broker_action_response(request, str(error))
        return await broker_action_response(request)

    @app.post(
        "/broker/actions/barrier/{name}", response_class=HTMLResponse, include_in_schema=False
    )
    async def broker_page_barrier(
        request: Request,
        name: str,
        time: str = Form(...),
    ) -> HTMLResponse:
        try:
            barrier_time = float(time)
            if barrier_time < 0:
                raise ValueError("barrier time must be non-negative")
            await run_in_threadpool(broker_service.set_time_barrier, name, barrier_time)
        except Exception as error:
            return await broker_action_response(request, str(error))
        return await broker_action_response(request)

    @app.post(
        "/broker/actions/barrier/{name}/clear", response_class=HTMLResponse, include_in_schema=False
    )
    async def broker_page_barrier_clear(request: Request, name: str) -> HTMLResponse:
        try:
            await run_in_threadpool(broker_service.clear_time_barrier, name)
        except Exception as error:
            return await broker_action_response(request, str(error))
        return await broker_action_response(request)

    @app.get("/api/v1/brokers", response_model=BrokerListResponse, tags=["brokers"])
    async def list_brokers() -> BrokerListResponse:
        return BrokerListResponse(brokers=await run_in_threadpool(broker_service.list))

    @app.post(
        "/api/v1/brokers",
        response_model=BrokerSummary,
        status_code=status.HTTP_201_CREATED,
        tags=["brokers"],
    )
    async def create_broker(request: BrokerCreateRequest) -> BrokerSummary:
        try:
            return await run_in_threadpool(broker_service.create, request)
        except BrokerAlreadyExistsError as error:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Broker '{error}' already exists",
            ) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error

    @app.get("/api/v1/brokers/{name}", response_model=BrokerSummary, tags=["brokers"])
    async def get_broker(name: str) -> BrokerSummary:
        try:
            return await run_in_threadpool(broker_service.summary, name)
        except BrokerNotFoundError as error:
            raise not_found(error) from error

    @app.get(
        "/api/v1/brokers/{name}/state",
        response_model=Union[CurrentStateQueryResponse, QueryResponse],
        tags=["queries"],
    )
    async def get_broker_state(
        name: str,
    ) -> Union[CurrentStateQueryResponse, QueryResponse]:
        """Return the broker's current HELICS state using the standard query."""
        try:
            value = await run_in_threadpool(
                broker_service.query,
                name,
                "root",
                "current_state",
            )
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return parse_query_response("root", "current_state", value)

    @app.get(
        "/api/v1/brokers/{name}/counts",
        response_model=Union[CountsQueryResponse, QueryResponse],
        tags=["queries"],
    )
    async def get_broker_counts(name: str) -> Union[CountsQueryResponse, QueryResponse]:
        """Return typed broker and interface counts."""
        try:
            value = await run_in_threadpool(
                broker_service.query,
                name,
                "root",
                "counts",
            )
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return parse_query_response("root", "counts", value)

    @app.get(
        "/api/v1/brokers/{name}/version",
        response_model=Union[StringQueryResponse, QueryResponse],
        tags=["queries"],
    )
    async def get_broker_version(name: str) -> Union[StringQueryResponse, QueryResponse]:
        """Return the HELICS version reported by the broker."""
        try:
            value = await run_in_threadpool(
                broker_service.query,
                name,
                "root",
                "version",
            )
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return parse_query_response("root", "version", value)

    @app.get(
        "/api/v1/brokers/{name}/connection",
        response_model=Union[IsConnectedQueryResponse, QueryResponse],
        tags=["queries"],
    )
    async def get_broker_connection(name: str) -> Union[IsConnectedQueryResponse, QueryResponse]:
        """Return the standard HELICS ``isconnected`` query as a boolean."""
        try:
            value = await run_in_threadpool(
                broker_service.query,
                name,
                "root",
                "isconnected",
            )
            return parse_query_response("root", "isconnected", value)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY, detail=str(error)
            ) from error

    @app.delete("/api/v1/brokers/{name}", status_code=status.HTTP_204_NO_CONTENT, tags=["brokers"])
    async def delete_broker(name: str) -> Response:
        try:
            await run_in_threadpool(broker_service.delete, name)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @app.post("/api/v1/brokers/{name}/query", response_model=QueryResponse, tags=["queries"])
    async def query_broker(name: str, request: QueryRequest) -> QueryResponse:
        try:
            value = await run_in_threadpool(
                broker_service.query,
                name,
                request.target,
                request.query,
            )
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return parse_query_response(request.target, request.query, value)

    @app.post("/api/v1/brokers/{name}/commands", response_model=ActionResponse, tags=["control"])
    async def send_command(name: str, request: CommandRequest) -> ActionResponse:
        try:
            await run_in_threadpool(
                broker_service.send_command, name, request.target, request.command
            )
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return ActionResponse()

    @app.put("/api/v1/brokers/{name}/time-barrier", response_model=ActionResponse, tags=["control"])
    async def set_time_barrier(name: str, request: TimeBarrierRequest) -> ActionResponse:
        try:
            await run_in_threadpool(broker_service.set_time_barrier, name, request.time)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return ActionResponse()

    @app.delete(
        "/api/v1/brokers/{name}/time-barrier", response_model=ActionResponse, tags=["control"]
    )
    async def clear_time_barrier(name: str) -> ActionResponse:
        try:
            await run_in_threadpool(broker_service.clear_time_barrier, name)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
            ) from error
        return ActionResponse()

    # Runner API ---------------------------------------------------------
    @app.get("/api/v1/runner/file", tags=["runner"])
    async def get_runner_file() -> object:
        try:
            value = await run_in_threadpool(runner.file)
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error
        return value or {}

    @app.post("/api/v1/runner/file", response_model=RunnerFileResponse, tags=["runner"])
    async def upload_runner_file(file: UploadFile = File(...)) -> RunnerFileResponse:
        try:
            value = await run_in_threadpool(runner.upload, await file.read(), file.filename)
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error
        return value

    @app.post("/api/v1/runner/file/name", tags=["runner"])
    async def set_runner_name(request: RunnerNameRequest) -> object:
        try:
            return await run_in_threadpool(runner.set_name, request.name) or {}
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.post("/api/v1/runner/file/folder", tags=["runner"])
    async def set_runner_folder(request: RunnerFolderRequest) -> object:
        try:
            return await run_in_threadpool(runner.set_folder, request.folder) or {}
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.post("/api/v1/runner/file/path", tags=["runner"])
    async def set_runner_path(request: RunnerPathRequest) -> object:
        try:
            return await run_in_threadpool(runner.set_path, request.path) or {}
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.post("/api/v1/runner/file/edit", response_model=RunnerFileResponse, tags=["runner"])
    async def add_runner_federate(request: RunnerFederateEdit) -> RunnerFileResponse:
        try:
            return await run_in_threadpool(runner.edit, request, "add")
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.put("/api/v1/runner/file/edit", response_model=RunnerFileResponse, tags=["runner"])
    async def update_runner_federate(request: RunnerFederateEdit) -> RunnerFileResponse:
        try:
            return await run_in_threadpool(runner.edit, request, "update")
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.delete("/api/v1/runner/file/edit", response_model=RunnerFileResponse, tags=["runner"])
    async def delete_runner_federate(request: RunnerFederateEdit) -> RunnerFileResponse:
        try:
            return await run_in_threadpool(runner.edit, request, "delete")
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.get("/api/v1/runner/log/{name}", response_model=LogResponse, tags=["runner"])
    async def get_runner_log(name: str) -> LogResponse:
        try:
            value = await run_in_threadpool(runner.log, name)
        except RunnerFileError as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
        return LogResponse(log=value)

    @app.get(
        "/api/v1/runner/run",
        response_model=RunnerRunResponse,
        response_model_exclude_none=True,
        tags=["runner"],
    )
    async def get_runner_status() -> RunnerRunResponse:
        running = await run_in_threadpool(runner.status)
        process = await run_in_threadpool(runner.process_info) if running else None
        return RunnerRunResponse(status=running, process=process)

    @app.post(
        "/api/v1/runner/run",
        response_model=RunnerRunResponse,
        response_model_exclude_none=True,
        tags=["runner"],
    )
    async def start_runner() -> RunnerRunResponse:
        try:
            value = await run_in_threadpool(runner.run)
        except RunnerFileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error
        return RunnerRunResponse(status=value, process=await run_in_threadpool(runner.process_info))

    @app.delete(
        "/api/v1/runner/run",
        response_model=RunnerRunResponse,
        response_model_exclude_none=True,
        tags=["runner"],
    )
    async def stop_runner() -> RunnerRunResponse:
        return RunnerRunResponse(status=await run_in_threadpool(runner.stop))

    @app.delete(
        "/api/v1/runner/broker",
        response_model=RunnerRunResponse,
        response_model_exclude_none=True,
        tags=["runner"],
        summary="Stop a runner-owned automatic broker",
        description=(
            "Stops the complete runner process group.  An automatic broker is "
            "never terminated independently of the federates that it serves."
        ),
    )
    async def stop_runner_broker() -> RunnerRunResponse:
        return RunnerRunResponse(status=await run_in_threadpool(runner.stop_broker))

    @app.get("/api/v1/runner/status", response_model=RunnerStatusResponse, tags=["runner"])
    async def get_federate_status(name: str) -> RunnerStatusResponse:
        return await run_in_threadpool(runner.get_status, name)

    @app.post("/api/v1/runner/status", response_model=RunnerStatusResponse, tags=["runner"])
    async def set_federate_status(request: RunnerStatusRequest) -> RunnerStatusResponse:
        return await run_in_threadpool(runner.set_status, request.name, request.status)

    # Observer database API ---------------------------------------------
    def observer_error(error: ObserverDatabaseError) -> HTTPException:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))

    @app.get("/api/v1/observer/database", response_model=DatabaseInfo, tags=["observer"])
    async def get_observer_database() -> DatabaseInfo:
        return DatabaseInfo(**await run_in_threadpool(observer.info))

    @app.post("/api/v1/observer/database", response_model=DatabaseInfo, tags=["observer"])
    async def upload_observer_database(file: UploadFile = File(...)) -> DatabaseInfo:
        try:
            value = await run_in_threadpool(observer.upload, await file.read())
        except ObserverDatabaseError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error
        return DatabaseInfo(**value)

    @app.get("/api/v1/observer/systeminfo", tags=["observer"])
    async def observer_system_info() -> object:
        try:
            return await run_in_threadpool(observer.system_info)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/cores", tags=["observer"])
    async def observer_cores() -> list[dict]:
        try:
            return await run_in_threadpool(observer.cores)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/federates", tags=["observer"])
    async def observer_federates() -> list[dict]:
        try:
            return await run_in_threadpool(observer.federates)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/graphs", tags=["observer"])
    async def observer_graphs() -> dict:
        try:
            return await run_in_threadpool(observer.graphs)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/subscriptions", tags=["observer"])
    async def observer_subscriptions() -> list[dict]:
        try:
            return await run_in_threadpool(observer.subscriptions)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/inputs", tags=["observer"])
    async def observer_inputs() -> list[dict]:
        try:
            return await run_in_threadpool(observer.inputs)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/publications", tags=["observer"])
    async def observer_publications() -> list[dict]:
        try:
            return await run_in_threadpool(observer.publications)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    @app.get("/api/v1/observer/data", tags=["observer"])
    async def observer_data() -> list[dict]:
        try:
            return await run_in_threadpool(observer.data)
        except ObserverDatabaseError as error:
            raise observer_error(error) from error

    # Profiler API -------------------------------------------------------
    @app.get("/api/v1/profile", tags=["profile"])
    async def get_profile() -> dict:
        try:
            return await run_in_threadpool(profiler.parse)
        except ProfileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error

    @app.post("/api/v1/profile", response_model=UploadResponse, tags=["profile"])
    async def upload_profile(file: UploadFile = File(...)) -> UploadResponse:
        try:
            await run_in_threadpool(profiler.upload, await file.read())
        except ProfileError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)
            ) from error
        return UploadResponse(path=str(profiler.path))

    @app.delete("/api/v1/profile", response_model=UploadResponse, tags=["profile"])
    async def clear_profile() -> UploadResponse:
        await run_in_threadpool(profiler.clear)
        return UploadResponse()

    # Serve the optional Svelte build from the same origin.  CI and release
    # builds place assets in either helics/webserver/static or the legacy
    # extras package; the latter is supported while that package is retired.
    static_dir = _find_static_dir()
    if static_dir is not None:
        app.mount("/", StaticFiles(directory=static_dir, html=True), name="web-ui")
    else:

        @app.get("/", include_in_schema=False, response_class=HTMLResponse)
        async def web_ui_unavailable() -> str:
            return "<h1>HELICS server</h1><p>Web UI assets are not installed. Use <a href='/docs'>/docs</a>.</p>"

    return app


def _find_static_dir() -> Optional[str]:
    """Find packaged Svelte assets without importing the legacy Flask app."""
    configured = os.environ.get("HELICS_WEB_STATIC_DIR")
    candidates = []
    if configured:
        candidates.append(Path(configured).expanduser())
    candidates.append(Path(__file__).resolve().parent / "static")
    try:
        import importlib.util

        package = importlib.util.find_spec("helics_cli_extras")
        if package and package.submodule_search_locations:
            candidates.append(Path(next(iter(package.submodule_search_locations))) / "static")
    except (ImportError, StopIteration):
        pass
    for candidate in candidates:
        if candidate.is_dir() and (candidate / "index.html").exists():
            return str(candidate)
    return None


def run(
    host: str = "127.0.0.1",
    port: int = 8000,
    server_url: Optional[str] = None,
) -> None:
    """Run the HELICS FastAPI server.

    When no API base is supplied, runner subprocesses use this listener's
    port.  Binding to a wildcard address still uses loopback for local runner
    callbacks; callers serving behind a proxy can provide ``server_url``.
    """
    import uvicorn

    configured_url = server_url or os.environ.get("HELICS_CLI_SERVER_API")
    if configured_url is None:
        callback_host = "127.0.0.1" if host in {"0.0.0.0", "::"} else host
        configured_url = f"http://{callback_host}:{port}/api/v1"
    uvicorn.run(create_app(server_url=configured_url), host=host, port=port)


def main() -> None:
    """Console-script entry point for ``helics_server``."""
    run()

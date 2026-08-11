"""FastAPI application factory and command-line runner."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.concurrency import run_in_threadpool

from ..query_models import IsConnectedQueryResponse, parse_query_response
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
)


def create_app(service: Optional[BrokerService] = None) -> FastAPI:
    """Create the HELICS web API application.

    ``service`` is injectable so callers can test or embed the application
    without sharing global broker state.
    """
    broker_service = service or BrokerService()

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        yield
        await run_in_threadpool(broker_service.shutdown)

    app = FastAPI(
        title="HELICS Server API",
        version="1.0.0",
        description="Manage HELICS brokers and inspect local federations.",
        lifespan=lifespan,
    )

    def not_found(error: BrokerNotFoundError) -> HTTPException:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Broker '{error}' not found")

    @app.get("/api/v1/health", response_model=HealthResponse, tags=["system"])
    async def health() -> HealthResponse:
        return HealthResponse()

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
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error

    @app.get("/api/v1/brokers/{name}", response_model=BrokerSummary, tags=["brokers"])
    async def get_broker(name: str) -> BrokerSummary:
        try:
            return await run_in_threadpool(broker_service.summary, name)
        except BrokerNotFoundError as error:
            raise not_found(error) from error

    @app.get("/api/v1/brokers/{name}/state", response_model=QueryResponse, tags=["queries"])
    async def get_broker_state(name: str) -> QueryResponse:
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
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
        return parse_query_response("root", "current_state", value)

    @app.get(
        "/api/v1/brokers/{name}/connection",
        response_model=IsConnectedQueryResponse,
        tags=["queries"],
    )
    async def get_broker_connection(name: str) -> IsConnectedQueryResponse:
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
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(error)) from error

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
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
        return parse_query_response(request.target, request.query, value)

    @app.post("/api/v1/brokers/{name}/commands", response_model=ActionResponse, tags=["control"])
    async def send_command(name: str, request: CommandRequest) -> ActionResponse:
        try:
            await run_in_threadpool(broker_service.send_command, name, request.target, request.command)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
        return ActionResponse()

    @app.put("/api/v1/brokers/{name}/time-barrier", response_model=ActionResponse, tags=["control"])
    async def set_time_barrier(name: str, request: TimeBarrierRequest) -> ActionResponse:
        try:
            await run_in_threadpool(broker_service.set_time_barrier, name, request.time)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
        return ActionResponse()

    @app.delete("/api/v1/brokers/{name}/time-barrier", response_model=ActionResponse, tags=["control"])
    async def clear_time_barrier(name: str) -> ActionResponse:
        try:
            await run_in_threadpool(broker_service.clear_time_barrier, name)
        except BrokerNotFoundError as error:
            raise not_found(error) from error
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error
        return ActionResponse()

    return app


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run the HELICS FastAPI server."""
    import uvicorn

    uvicorn.run(create_app(), host=host, port=port)


def main() -> None:
    """Console-script entry point for ``helics_server``."""
    run()

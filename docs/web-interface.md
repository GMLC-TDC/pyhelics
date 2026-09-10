# Web server API

The experimental HELICS web server is a FastAPI application that manages
brokers in the current Python process.  It is the replacement path for the
former Flask application and does not start `helics_broker_server --http`.

The staged migration, including the work required before the native C++
webserver can be removed from HELICS, is tracked in the
[webserver migration plan](webserver-migration-plan.md).

Install the optional server dependencies and start the application:

```bash
pip install "helics[server]"
helics server
```

By default the server binds to `127.0.0.1:8000` and opens its interactive
OpenAPI documentation at `http://127.0.0.1:8000/docs`.  Use `--host`, `--port`,
`--server-url`, and `--no-open` to configure the listener and runner callback
API base.  Without `--server-url`, the service derives the base from the
listener port.  When the optional Svelte build is
installed, the same process serves the dashboard at `/`; otherwise `/docs`
remains available for API-only deployments.

The broker page prototype at `/broker` is rendered with Jinja2 and updated
with HTMX.  It is intentionally implemented alongside the Svelte build so the
interaction and maintenance trade-offs can be evaluated before migrating the
remaining pages.

## Broker API

All endpoints are under `/api/v1`.  The initial API exposes broker lifecycle
and control operations:

| Operation | Endpoint |
| --- | --- |
| Service health | `GET /api/v1/health` |
| List local brokers | `GET /api/v1/brokers` |
| Create a broker | `POST /api/v1/brokers` |
| Inspect/delete a broker | `GET`/`DELETE /api/v1/brokers/{name}` |
| Inspect current broker state | `GET /api/v1/brokers/{name}/state` |
| Inspect broker counts | `GET /api/v1/brokers/{name}/counts` |
| Inspect HELICS version | `GET /api/v1/brokers/{name}/version` |
| Inspect connection status | `GET /api/v1/brokers/{name}/connection` |
| Execute a HELICS query | `POST /api/v1/brokers/{name}/query` |
| Send a command | `POST /api/v1/brokers/{name}/commands` |
| Set/clear a time barrier | `PUT`/`DELETE /api/v1/brokers/{name}/time-barrier` |

Runner, observer, and profile capabilities are also exposed under the same
versioned API:

| Capability | Endpoints |
| --- | --- |
| Runner file and process lifecycle | `/api/v1/runner/*` |
| Observer database upload and views | `/api/v1/observer/*` |
| Profile upload, parsing, and clear | `/api/v1/profile` |
| Stop a runner-owned automatic broker | `DELETE /api/v1/runner/broker` |

Runner endpoints accept and return typed Pydantic models.  A runner upload is
validated before it is written: federate names must be unique, executable
strings and environment values cannot be blank, uploaded names must be a
single `.json` basename, and every federate working directory must exist before
launch.  The legacy top-level `name` field is optional (the CLI falls back to
the runner filename).  Relative working and logging paths are resolved from the runner file;
logging directories are created when a run starts.

`POST /api/v1/runner/run` launches `helics run` with structured arguments and
returns the owned process metadata (PID, runner path, API base, and whether the
configuration requested an automatic broker).  The service starts that
process in a new process group/session.  `DELETE /api/v1/runner/run` and
application shutdown terminate the entire group, including federates and an
auto-created broker, so the service never leaves a run-owned broker behind.
`DELETE /api/v1/runner/broker` is a constrained alias for the same cleanup and
only acts when the active runner configuration owns an automatic broker; there
is no process-wide broker kill operation.

The API base passed to the runner is configurable with the `server_url`
argument to `RunnerService`/`create_app` or the `HELICS_CLI_SERVER_API`
environment variable.  It defaults to `http://127.0.0.1:8000/api/v1`.

For example, create a local ZMQ broker that expects two federates:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/brokers \
  -H "Content-Type: application/json" \
  -d '{"name":"example", "core_type":"zmq", "num_federates":2}'
```

HELICS 3.7 startup controls are available as typed request fields:
`local_federates`, `local_subbrokers`, and `required_federates` (a list of
federate names).  They map to the corresponding broker options and can be
combined with `num_federates` when a hierarchy has both local and forwarded
participants.

The server owns only brokers it creates.  It does not discover or control
brokers started by another process.

The former Flask `/api/observer`, `/api/runner`, `/api/profiler`, and
`/api/broker-server` endpoints are no longer provided.  Clients should use the
versioned routes above and the same-origin API when the bundled UI is served.

## Typed HELICS queries

Standard HELICS queries progressively receive Pydantic response models in
`helics.query_models`.  Typed models currently cover common scalar, list,
state, count, status, and version queries.  The `isconnected` query is
available as both the generic query request and the convenient
`GET /brokers/{name}/connection` endpoint.  Its response is always:

```json
{"target": "root", "query": "isconnected", "value": true}
```

Queries without a registered model remain available through `POST .../query`
with the common `{target, query, value}` envelope.  This lets the API expose
custom and newer HELICS queries immediately while their stable Pydantic models
are added independently.

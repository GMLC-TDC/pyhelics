# HELICS web server

The experimental HELICS web server is a FastAPI application for managing
service-owned brokers, runner jobs, observer database artifacts, and profile
data. It replaces the former Flask application. It does not start or depend on
the native HELICS broker HTTP management server.

The native server removal plan is tracked in the
[webserver migration plan](webserver-migration-plan.md). HELICS HTTP and
WebSocket core transports are separate features and are not part of that
removal.

## Start the service

Install the optional server dependencies and launch the service:

```bash
pip install "helics[server]"
helics server
```

The service listens on `127.0.0.1:8000` by default, opens the interactive API
documentation at `http://127.0.0.1:8000/docs`, and serves the bundled Svelte UI
at `http://127.0.0.1:8000/`. The machine-readable OpenAPI document is at
`/openapi.json`.

Use `--host`, `--port`, and `--no-open` to configure the listener and browser
behavior. The runner callback API base normally follows the listener address
and port. Set `--server-url` when the service is behind a proxy or its public
API address differs from the listener address:

```bash
helics server --host 0.0.0.0 --port 9000 \
  --server-url https://helics.example.org/api/v1 --no-open
```

The `/broker` page is a separate Jinja2/HTMX broker-management prototype. It
currently lives alongside the Svelte application so the simpler server-rendered
approach can be evaluated before deciding whether to migrate the remaining UI.

The Svelte source and browser tests live in the repository's `client/`
directory. Its production build is bundled in `helics/webserver/static/` and
served by FastAPI; no `helics-cli-extras` installation is needed. The separate
extras distribution remains installable as a deprecated no-op compatibility
shim for existing installation scripts.

## Configuration and deployment

| Setting | Purpose |
| --- | --- |
| `HELICS_CLI_SERVER_API` | Default API base for `helics run --connect-server` and runner subprocesses. Defaults to `http://127.0.0.1:8000/api/v1`. |
| `HELICS_WEB_CORS_ORIGINS` | Comma-separated browser origins allowed by the server. The development defaults are `http://localhost:5173` and `http://127.0.0.1:5173`. |
| `HELICS_WEB_STATIC_DIR` | Optional directory override for the built Svelte assets. |

When services are created without an explicit storage directory, runner files,
observer databases, and profile files are stored under `__helics-server` in
the server's current working directory. Uploaded runner, observer, and profile
artifacts remain on disk after shutdown. A new observer database or profile
upload replaces the prior artifact; `DELETE /api/v1/profile` removes the
profile. Runner configuration and logs are not automatically deleted.

The default listener is loopback-only. The service has no authentication,
authorization, or TLS. Do not expose it directly to an untrusted network. For
remote access, use a protected reverse proxy and restrict CORS to the browser
origins that need access. CORS is not an authentication mechanism.

At shutdown, the service disconnects brokers it created and stops the process
group for a run it started. It does not discover or adopt brokers created by
other processes. Status changes are read through polling endpoints; the API
does not currently provide a streaming event protocol.

## API overview

All JSON API endpoints use the `/api/v1` prefix. Interactive documentation at
`/docs` includes request and response schemas and can issue requests to the
running service.

### Brokers

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/v1/health` | Check service health |
| `GET` | `/api/v1/brokers` | List brokers created by this service |
| `POST` | `/api/v1/brokers` | Create a broker |
| `GET`, `DELETE` | `/api/v1/brokers/{name}` | Inspect or disconnect a managed broker |
| `GET` | `/api/v1/brokers/{name}/state` | Query current federation state |
| `GET` | `/api/v1/brokers/{name}/counts` | Query broker and federation counts |
| `GET` | `/api/v1/brokers/{name}/version` | Query the HELICS version |
| `GET` | `/api/v1/brokers/{name}/connection` | Query whether the broker is connected |
| `POST` | `/api/v1/brokers/{name}/query` | Run a HELICS query |
| `POST` | `/api/v1/brokers/{name}/commands` | Send a command to a broker target |
| `PUT`, `DELETE` | `/api/v1/brokers/{name}/time-barrier` | Set or clear a time barrier |

For example, create a ZMQ broker expecting two federates:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/brokers \
  -H "Content-Type: application/json" \
  -d '{"name":"example", "core_type":"zmq", "num_federates":2}'
```

Broker creation also accepts `arguments`, `num_brokers`, `local_federates`,
`local_subbrokers`, `required_federates`, `port`, `interface`, and `log_level`.
The 3.7 startup fields map to their corresponding HELICS broker options.
`required_federates` is a list of names. A broker summary includes its address,
connection state, root status, whether it accepts new federates, and explicit
managed ownership metadata.

Run a query against a managed broker with a JSON request:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/brokers/example/query \
  -H "Content-Type: application/json" \
  -d '{"target":"root", "query":"current_state"}'
```

The response uses the common query envelope, for example
`{"target":"root","query":"current_state","value":{...}}`.

The service can only list and control brokers it created. The Python
`BrokerFactory` is process-local, so this service cannot use it to discover or
adopt a broker started by another process.

### Runner

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET`, `POST` | `/api/v1/runner/file` | Read the selected configuration or upload a JSON runner file |
| `POST` | `/api/v1/runner/file/name` | Select the runner filename |
| `POST` | `/api/v1/runner/file/folder` | Select the runner folder |
| `POST` | `/api/v1/runner/file/path` | Select an existing runner file |
| `POST`, `PUT`, `DELETE` | `/api/v1/runner/file/edit` | Add, update, or remove a federate entry |
| `GET` | `/api/v1/runner/log/{name}` | Read a federate log |
| `GET`, `POST`, `DELETE` | `/api/v1/runner/run` | Inspect, start, or stop the active run |
| `DELETE` | `/api/v1/runner/broker` | Stop the run when it owns an automatic broker |
| `GET`, `POST` | `/api/v1/runner/status` | Read or update a federate status |

Runner configuration is validated before saving and again before launch.
Federate names must be unique, executable and environment values must be
valid, and an uploaded filename must be a single `.json` basename. Relative
working and logging paths are resolved from the runner file. Each federate
working directory must exist before launch; the logging directory is created
when the run starts.

`POST /api/v1/runner/run` starts `helics run` with structured process
arguments, without shell expansion. The response includes the process ID,
runner path, callback API base, and whether the configuration requested an
automatic broker. The service owns the process group, including its federates
and automatic broker, and stops the group on `DELETE /api/v1/runner/run` or
service shutdown. The broker endpoint is deliberately limited to a broker
owned by the active runner; it does not kill unrelated brokers.

The CLI callback base can be set with `helics run --server-url URL` or
`HELICS_CLI_SERVER_API`. The value defaults to
`http://127.0.0.1:8000/api/v1`.

### Observer data and profiles

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET`, `POST` | `/api/v1/observer/database` | Inspect or upload the observer SQLite database |
| `GET` | `/api/v1/observer/systeminfo` | Read recorded HELICS system information |
| `GET` | `/api/v1/observer/cores` | Read recorded cores |
| `GET` | `/api/v1/observer/federates` | Read recorded federates |
| `GET` | `/api/v1/observer/graphs` | Read the federate and data graphs |
| `GET` | `/api/v1/observer/subscriptions` | Read recorded subscriptions |
| `GET` | `/api/v1/observer/inputs` | Read recorded inputs |
| `GET` | `/api/v1/observer/publications` | Read recorded publications |
| `GET` | `/api/v1/observer/data` | Read recorded data rows |
| `GET`, `POST`, `DELETE` | `/api/v1/profile` | Read, upload, or clear profile data |

The observer API reads an uploaded database; it does not start or control the
observer federate. Use `helics observer` to collect data. Database rows retain
their recorded fields because available columns vary with HELICS versions and
the federation being observed. Profile uploads must be non-empty UTF-8 text;
parsing reports an error if a non-empty line does not match the supported
profile format.

## Response models and compatibility

Request validation and many response bodies use Pydantic models. The current
model coverage is visible in `/openapi.json`. Query responses use a common
`{target, query, value}` envelope. Common scalar, list, state, count, status,
and version queries have typed values. Custom queries and structured query
values without a stable nested model remain flexible JSON so newer HELICS
queries can still be used.

Observer records are also flexible JSON because database fields vary. Some
runner file, observer read, and profile read routes expose inferred JSON
structures instead of complete named response models. Complete nested
Pydantic coverage for every HELICS query and every API response remains
planned work; the API schema should be checked when relying on a specific
response shape.

Service errors generally return `{"detail": "..."}`. Request validation
errors use FastAPI's standard `422` response, which includes validation
locations and messages. A missing broker or unavailable observer database
returns `404`; a duplicate broker name returns `409`.

The former Flask `/api/observer`, `/api/runner`, `/api/profiler`, and
`/api/broker-server` routes are not provided. Clients should use the versioned
routes above. The web server remains experimental; consult the migration plan
for the work required before the native HELICS management webserver can be
removed.

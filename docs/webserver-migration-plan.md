# Webserver migration and HELICS removal plan

This document records the plan for moving the HELICS management webserver from
the C++ HELICS repository into pyhelics.  The native HELICS webserver is not to
be removed until a pyhelics release contains the replacement service and its
supported interface.

## Objective

Provide one maintained Python service that combines:

- broker lifecycle and control;
- HELICS queries and typed responses;
- the existing runner workflow;
- observer data and topology views; and
- profiler results and the existing web UI.

The replacement should use FastAPI and Pydantic, expose a documented `/api/v1`
interface, and serve the web UI from the same application.  The old Flask
application, the embedded C++ HTTP management layer, and their obsolete
dependencies can then be retired in a controlled release sequence.

This plan concerns the embedded management webserver.  HELICS `HTTP` and
`WEBSOCKET` core transports are separate networking features and should not be
removed unless a separate compatibility decision is made.

## Current baseline

The `webserver` branch already contains the first FastAPI vertical slice:

- `helics.webserver.create_app()` and `helics server` start a Uvicorn service.
- Brokers created by the service can be listed, inspected, queried, commanded,
  barrier-controlled, and deleted.
- Broker summaries use the HELICS 3.7 `is_root` and
  `is_open_to_new_federates` bindings.
- Common query responses have Pydantic envelopes and a registry in
  `helics.query_models`.
- Unit and real-broker integration tests cover the broker/control slice.
- The service owns only brokers it creates; it does not discover arbitrary
  externally started brokers.

The Flask application and its Flask dependencies have now been removed from
`helics_cli_extras`.  Its Svelte client is being migrated and still needs a
rebuilt asset bundle; the source previously called Flask on port 5000 and the
native HELICS server on port 8080.  FastAPI now contains replacement runner,
observer-database, profile, and broker routes, but the full UI and observer
federate lifecycle still require integration testing.

The runner replacement now validates typed `RunnerConfig` and
`RunnerFederateConfig` models, rejects unsafe upload/path inputs, passes a
structured argv to `helics run`, and propagates a configurable FastAPI API
base.  Each run is started in an owned process group/session; stopping the run
or shutting down the service cleans up its federates and any auto-created
broker.  Runner status and log endpoints use typed response models.  Remaining
runner work is cross-platform process-tree integration coverage and browser
smoke coverage for the final bundled UI.

A Jinja2/HTMX broker-page prototype is available at `/broker`.  It is served
directly by FastAPI and is being evaluated as a lower-maintenance alternative
to keeping a JavaScript framework for the entire UI.

## HELICS 3.7 compatibility audit

The public C API delta from HELICS 3.6.1 to 3.7.0 is now covered in pyhelics:

- broker/core root and open-to-new-federates functions are wrapped and used by
  broker summaries;
- `HELICS_PROPERTY_INT_VALUE_BUFFER_WARNING` is exposed through
  `HelicsProperty` and its module aliases;
- the corrected global-input return types are represented as `HelicsInput`;
- `HELICS_BIG_NUMBER`, `HELICS_MAX_TIME_VALUE`,
  `HELICS_TERMINATION_TIME_VALUE`, `HELICS_TIME_BIGTIME`, and
  `HELICS_TIME_TERMINATION` are exposed as Python constants;
- broker startup controls (`local_federates`, `local_subbrokers`, and
  `required_federates`) are typed by the FastAPI broker request and the
  Jinja2 form.

The remaining 3.7 work is verification rather than a new binding surface:
test the `raw`/`map`/`custom` data-type aliases and the timing/iteration fixes
against a released 3.7 runtime, and keep the build dependencies at C++20 and
Boost 1.83 or newer.  A locally present, ignored `helics-src` directory can
override the release download; it must be refreshed to 3.7.0 (or removed) when
testing a linked HELICS checkout.

## Migration phases

### 1. Freeze the replacement contract

- Keep all new endpoints under `/api/v1`.
- Use consistent snake_case JSON fields, standard HTTP methods, and one typed
  error envelope.
- Define broker ownership explicitly.  The initial supported mode may be
  service-managed brokers only; external-broker attach/discovery must either be
  implemented in HELICS/pyhelics or documented as unsupported.
- Decide whether event updates use polling, Server-Sent Events, or WebSockets.
- Define host, port, CORS, authentication, upload limits, and shutdown behavior
  before exposing the service beyond localhost.

### 2. Complete the Python services

Add services and Pydantic models to the FastAPI application for:

- **Runner (implemented):** file/configuration management, run lifecycle,
  logs, status, and deterministic process-group cleanup.  The service uses
  structured subprocess arguments, path validation, and explicit broker
  ownership; it does not recreate the old shell-command behavior.  Remaining
  work is cross-platform process-tree integration coverage.
- **Observer:** observer startup/control plus typed access to system info,
  cores, federates, publications, inputs, subscriptions, graphs, and recorded
  data.  Validate SQLite uploads and document retention/cleanup behavior.
- **Profiler:** robust parsing and typed event/interval/statistic responses,
  including clear errors for missing or malformed profile data.
- **Queries:** replace the remaining `Dict[str, Any]` structures with nested
  models for state, counts, status, federate maps, dependency/data-flow
  graphs, interface details, logs, and time-debugging responses.  Preserve a
  generic envelope for custom or newer HELICS queries.

Update `helics run --connect-server` and its status checker to use a
configurable FastAPI server URL and the new runner endpoints.

### 3. Unify and serve the UI

- Mount the built Svelte application and provide an SPA fallback from FastAPI.
- Replace hard-coded `5000`/`8080` URLs with same-origin `/api/v1` calls.
- Adapt the client to the snake_case response contract.
- Remove the separate native broker-server start/stop controls; the combined
  service should own broker lifecycle through its broker API.
- Build the client in CI and include its assets in the pyhelics distribution.
- Add a development mode with narrowly scoped CORS; production should normally
  use same-origin requests.

### 4. Test the replacement

Maintain a behavior matrix against the meaningful native webserver behavior.
The nonstandard URL/body variants and `SEARCH` method do not need to be
preserved if the new interface is clearer.

Required tests include:

- OpenAPI schema and request/response validation;
- broker lifecycle, ownership, concurrency, errors, and shutdown;
- real HELICS broker/federate query, command, and barrier behavior;
- runner process cleanup, logs, status transitions, and invalid paths (the
  service-level coverage is in `tests/test_webserver_services.py`; cross-platform
  process-tree and browser smoke coverage remain);
- observer database upload, topology, and recorded-data reads;
- profiler parsing and malformed-input handling;
- UI build, static serving, SPA routing, and browser-level smoke tests;
- CI coverage with released HELICS 3.7 wheels on every supported platform;
- installation without Flask and verification that no legacy endpoint is used.

### 5. Deprecate and remove old Python layers

The first part of this phase is complete: the Flask application has been
removed and the UI is being switched to the versioned FastAPI routes.  Before
publishing the combined service as the default, complete the remaining cleanup:

- remove unused `requests` and `pandas` dependencies (after confirming no
  public API relies on them);
- retain SQLAlchemy only if it remains necessary for the observer writer, and
  remove the Flask automap/read path;
- decide whether the maintained observer/runner code should remain in
  `helics_cli_extras` or be folded into `helics`;
- publish an updated `helics-cli-extras` wheel before updating any release that
  still installs that package, so PyPI users do not receive the old Flask
  dependency;
- update installation, CLI, examples, release notes, and a migration guide.

### 6. Remove the native HELICS webserver

This phase occurs only after a pyhelics release with the replacement service is
available and the migration tests pass.

In HELICS, remove or replace:

- `helicsWebServer.cpp/.hpp` and `indexPage.hpp`;
- `RestApiConnection.cpp/.hpp`;
- webserver CMake options, compile definitions, and conditional test targets;
- broker application `--http`, `--web`, `--websocket`, and webserver-argument
  flags that exist only for the management server;
- native webserver documentation and help text;
- the broker remote-terminal path that depends on `RestApiConnection` (port it
  to a Python HTTP client or intentionally retire it).

Keep the independent HELICS HTTP/WEBSOCKET core transports.  Update the HELICS
release notes and pyhelics `helics_version.cmake` to the first release in which
the native management server has been removed.  Remove the pyhelics build
warning that currently refers to a missing native webserver.

## Release and rollback strategy

1. Ship the FastAPI service behind the optional `server` extra while the
   remaining UI migration is completed.
2. Publish endpoint and configuration migration notes for users of the former
   Flask/native management APIs.
3. Make the combined FastAPI service the documented/default path and verify the
   UI and CLI against it in CI.
4. Remove any remaining legacy Python compatibility code in a subsequent
   pyhelics release.
5. Remove the native server in a HELICS release after the completed pyhelics
   release is available.

At each step, retain a versioned API contract and a tested rollback path so a
HELICS upgrade does not strand existing pyhelics users.

## Definition of complete migration

The migration is complete when `pip install "helics[server]"` followed by
`helics server` serves the UI and all supported management APIs; no client code
depends on ports 5000 or 8080; responses and errors are documented Pydantic
models; Flask and its obsolete dependencies are gone; HELICS builds without
the embedded management webserver; and the full Python, UI, and cross-platform
integration suites pass.

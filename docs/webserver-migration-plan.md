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

The `webserver` branch contains a working FastAPI service and bundled web UI:

- `helics.webserver.create_app()` and `helics server` start a Uvicorn service.
- Brokers created by the service can be listed, inspected, queried, commanded,
  barrier-controlled, and deleted.
- Broker summaries use the HELICS 3.7 `is_root` and
  `is_open_to_new_federates` bindings.
- Common query responses have Pydantic envelopes and a registry in
  `helics.query_models`.
- Unit and real-broker integration tests cover the broker/control slice.
- The service owns only brokers it creates; it does not discover arbitrary
  externally started brokers.  Same-process `BrokerFactory` discovery and
  broker adoption are intentionally deferred and are not required for the
  native webserver replacement.

The Flask application and its Flask dependencies have now been removed from
`helics_cli_extras`.  The maintained observer federate now lives in
`helics.observer`; `helics_cli_extras` 0.0.3 remains only as a compatibility
package that re-exports the observer and database models.  The Svelte client
is built into the FastAPI package, and its source previously called Flask on
port 5000 and the native HELICS server on port 8080.  FastAPI now contains
replacement runner, observer-database, profile, and broker routes.

The runner replacement validates typed `RunnerConfig` and
`RunnerFederateConfig` models, rejects unsafe upload/path inputs, passes
structured arguments to `helics run`, and propagates a configurable FastAPI
API base. Each run is started in an owned process group/session; stopping the
run or shutting down the service cleans up its federates and any automatic
broker. Runner status and log endpoints use typed response models. Service
tests cover process ownership and cleanup; cross-platform process-tree
integration coverage remains a release validation item. The bundled UI has a
Playwright smoke test in CI.

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
- Define broker ownership explicitly.  The initial supported mode is
  service-managed brokers only.  External-broker attach/discovery is
  documented as unsupported and deferred; it is not a requirement for
  removing the native management webserver.
- Use polling for status updates in the initial release; streaming events are
  deferred until a concrete UI requirement exists.
- The default listener is loopback-only and has no built-in authentication;
  non-loopback deployments must use a protected reverse proxy or equivalent.
  CORS, upload validation, and shutdown cleanup are defined by the FastAPI
  service and covered by its contract tests.

### 2. Complete the Python services

Implementations and remaining contract work:

- **Runner (implemented):** configuration upload/editing, run lifecycle, logs,
  status, path validation, structured subprocess arguments, and owned
  process-group cleanup are available. Add cross-platform integration tests
  that verify child processes and automatic brokers are stopped reliably.
- **Observer database (implemented):** SQLite upload and read routes expose
  system information, cores, federates, graphs, subscriptions, inputs,
  publications, and recorded data. The API reads observer output; starting and
  controlling the observer remains the `helics observer` CLI workflow. Rows
  retain flexible fields because database schemas vary.
- **Profile (implemented with typed-model follow-up):** upload, parse, and
  clear operations are available. Align the declared profile model with the
  current unwrapped per-federate JSON response before adding it to the route
  contract, and keep malformed-input behavior covered.
- **Queries (partially implemented):** a common Pydantic envelope and typed
  models cover common scalar, list, state, count, status, and version queries.
  Add nested models for the remaining structured queries where their schemas
  are stable; keep flexible values for custom and newer queries.
- **API responses (remaining):** add explicit response models to routes that
  currently rely on inferred dictionaries or generic JSON, while preserving
  flexible shapes for observer database rows and custom queries.

The CLI and its status checker now use the configurable FastAPI API base via
`--server-url` or `HELICS_CLI_SERVER_API`.

### 3. Unify and serve the UI

The combined application serves the built Svelte UI and its API from one
origin. The client uses the versioned `/api/v1` routes; the former separate
Flask and native broker-server controls have been removed. CI builds the UI,
checks the packaged assets, and runs a Playwright smoke test. Development CORS
origins can be configured with `HELICS_WEB_CORS_ORIGINS`; normal deployments
should use same-origin requests. The `/broker` Jinja2/HTMX page is a separate
prototype and does not replace the Svelte pages yet.

### 4. Test the replacement

Maintain a behavior matrix against the meaningful native webserver behavior.
The nonstandard URL/body variants and `SEARCH` method do not need to be
preserved if the new interface is clearer.

Required tests include:

- OpenAPI schema and request/response validation (nested response-model
  coverage is still being expanded);
- broker lifecycle, ownership, concurrency, errors, and shutdown;
- real HELICS broker/federate query, command, and barrier behavior;
- runner process cleanup, logs, status transitions, and invalid paths (the
  service-level coverage is in `tests/test_webserver_services.py`; the
  cross-platform process-group matrix remains a release validation task);
- observer database upload, topology, and recorded-data reads;
- profiler parsing and malformed-input handling;
- UI build, static serving, SPA routing, packaged-asset checks, and
  browser-level smoke tests;
- CI coverage with released HELICS 3.7 wheels on every supported platform;
- installation without Flask and verification that no legacy endpoint is used.

### 5. Deprecate and remove old Python layers

The Flask application has been removed and the UI uses the versioned FastAPI
routes. The observer writer has been folded into `helics`, while the separately
published extras package remains a compatibility shim. Remaining cleanup is
to publish the updated compatibility wheel and remove the shim after its
compatibility window:

- `requests`, `pandas`, Flask, and the Flask automap/read path are no longer
  dependencies; SQLAlchemy is retained only for the observer writer;
- publish the updated `helics-cli-extras` 0.0.3 compatibility wheel before
  updating any release that still imports that package;
- keep installation, CLI, examples, and migration documentation aligned with
  the supported interface; add release notes when preparing the package
  release.

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

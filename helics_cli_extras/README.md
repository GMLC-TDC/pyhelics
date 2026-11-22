# helics-cli-extras compatibility package

This package is deprecated. Its web UI and server are now included in the
main [`helics`](https://pypi.org/project/helics/) distribution. Install
`helics[server]` and run `helics server` for the combined FastAPI service.

Installing `helics-cli-extras` no longer installs or starts a separate web
application. `import helics_cli_extras` succeeds and emits a
`DeprecationWarning`, but the package exposes no functionality. The old
`helics[cli]` extra remains unchanged. Code that needs the observer should
import from `helics.observer` directly and install `helics[cli]`.

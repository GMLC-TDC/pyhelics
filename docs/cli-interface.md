# CLI interface

CLI for running Hierarchical Engine for Large-scale Infrastructure Co-Simulations (HELICS).

- Supports configurations of federates using plugins
- Allows running of federation using a runner configuration

![](https://user-images.githubusercontent.com/1813121/144665647-c95e653b-dbc6-410d-b653-2c7510294a76.png)

## Quick Examples

```bash
helics --help
```

```
Usage: helics [OPTIONS] COMMAND [ARGS]...

  HELICS command line interface

Options:
  --version      Show the version and exit.
  -v, --verbose
  --help         Show this message and exit.

Commands:
  observer
  profile-plot
  run           Run HELICS federation
  server
```

## Usage

```bash
helics run --path examples/pi-exchange/runner.json --profile
helics profile-plot examples/pi-exchange/profile.txt
```

When a run is launched from the FastAPI service, use
`helics run --connect-server --server-url URL` to select its API base.  The
same value can be supplied through `HELICS_CLI_SERVER_API`; the default is
`http://127.0.0.1:8000/api/v1`.

For a non-default listener, `helics server --port 9000` automatically points
run callbacks at port 9000; use `helics server --server-url URL` when the
service is behind a proxy or uses a different externally visible address.

::: mkdocs-click
    :module: helics.cli
    :command: cli
    :prog_name: helics
    :list_subcommands: True

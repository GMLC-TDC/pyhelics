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

::: mkdocs-click
    :module: helics.cli
    :command: cli
    :prog_name: helics
    :list_subcommands: True

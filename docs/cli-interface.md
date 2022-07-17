# CLI interface

CLI for running Hierarchical Engine for Large-scale Infrastructure Co-Simulations (HELICS).

- Supports configurations of federates using plugins
- Allows running of federation using a runner configuration

![](https://user-images.githubusercontent.com/1813121/144665647-c95e653b-dbc6-410d-b653-2c7510294a76.png)

### Documentation

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

```bash
helics run --help
```

```
Usage: helics run [OPTIONS]

  Run HELICS federation

Options:
  --path PATH                     Path to config.json that describes how to
                                  run a federation  [required]
  --silent
  --no-log-files
  --no-kill-on-error              Do not kill all federates on error
  -l, --broker-loglevel, --loglevel TEXT
                                  Log level for HELICS broker
  --profile                       Profile flag
  -w, --web                       Run the web interface on startup
  --help                          Show this message and exit.
```

```bash
$ helics profile-plot --help
```

```
Usage: helics profile-plot [OPTIONS]

Options:
  --path PATH  Path to profile.txt that describes profiling results of a
               federation  [required]
  --help       Show this message and exit.
```

### Usage

```bash
helics run --path examples/pi-exchange/runner.json --profile
helics profile-plot examples/pi-exchange/profile.txt
```

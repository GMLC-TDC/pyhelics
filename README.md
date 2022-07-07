# PyHELICS

[![](https://github.com/GMLC-TDC/pyhelics/workflows/CI/badge.svg)](https://github.com/GMLC-TDC/pyhelics/actions)
[![](https://badges.gitter.im/GMLC-TDC/pyhelics.png)](https://gitter.im/GMLC-TDC/HELICS)
[![](https://img.shields.io/badge/docs-ready-blue.svg)](https://python.helics.org)
[![](https://codecov.io/gh/GMLC-TDC/pyhelics/branch/main/graph/badge.svg)](https://codecov.io/gh/GMLC-TDC/pyhelics)
[![](https://img.shields.io/pypi/pyversions/helics)](https://pypi.org/project/helics/)
[![](https://img.shields.io/pypi/wheel/helics)](https://pypi.org/project/helics/)
[![](https://img.shields.io/pypi/v/helics)](https://pypi.org/project/helics/)
[![](https://img.shields.io/pypi/dm/helics)](https://pypi.org/project/helics/)

Python HELICS bindings

```bash
pip install helics
```

If you wish to get additional functionality in the CLI (_experimental_), you can install it using the following:

```bash
pip install 'helics[cli]'
```

# Documentation

To use the project:

```python
import helics as h
h.helicsGetVersion()
```

See <https://docs.helics.org> for more information about how to use HELICS.

This package uses `cffi` to provide a Python interface to the [HELICS C API](https://docs.helics.org/en/latest/references/api-reference/C_API.html).

By default, when you install from PyPI, the version number of the package will match the version of HELICS that is installed.
For example, if you run the following:

```
pip install helics
```

You will also get precompiled binaries of [HELICS](https://github.com/GMLC-TDC/HELICS/releases/latest) for your platform if they exist.
If they don't exist, a source distribution will attempt to be built and installed. The user can also provide the location of the binaries if they wish to do so.
For more information, see <https://python.helics.org/installation>.

# Debugging

Please share the output of the following command when creating an issue:

```
$ python -c "import helics as h; import json; print(json.dumps(h.helicsGetSystemInfo(), indent=4, sort_keys=True))"
```

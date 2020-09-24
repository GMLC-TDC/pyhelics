# PyHELICS

![CI](https://github.com/GMLC-TDC/pyhelics/workflows/CI/badge.svg)
[![image](https://badges.gitter.im/GMLC-TDC/pyhelics.png)](https://gitter.im/GMLC-TDC/HELICS)
[![image](https://img.shields.io/badge/docs-ready-blue.svg)](https://python.helics.org)
[![codecov](https://codecov.io/gh/GMLC-TDC/pyhelics/branch/master/graph/badge.svg)](https://codecov.io/gh/GMLC-TDC/pyhelics)

Python HELICS bindings

```bash
pip install helics
```

Documentation
=============

To use the project:

```python
import helics as h
h.helicsGetVersion()
```

See <https://docs.helics.org> for more information about how to use HELICS.

This package uses `cffi` to provide a Python interface to the [HELICS C API](https://docs.helics.org/en/latest/c-api-reference/index.html).

By default, when you install from PyPI, the version number of the package will match the version of HELICS that is installed.
For example, if you run the following:

```
pip install helics==2.6.0.post0.dev0
```

You will get the tagged release of this python package: [helics-v2.6.0.post0.dev0](https://github.com/GMLC-TDC/pyhelics/releases/tag/v2.6.0.post0.dev0).

You will also get precompiled binaries of [HELICS-v2.6.0](https://github.com/GMLC-TDC/HELICS/releases/tag/v2.6.0) for your platform if they exist.
If they don't exist, a source distribution will be installed in which case the user must provide the location of the binaries.
For more information, see <https://python.helics.org/installation>.

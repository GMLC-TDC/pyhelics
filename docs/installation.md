# Installation Instructions for developers

This package uses `cffi` to interface with the HELICS library.
The source for this package contains only pure python code.

**Download**

In order to run this package, you will need to download HELICS.

You can use this package to download HELICS.

```
git clone https://github.com/GMLC-TDC/pyhelics
cd pyhelics
python setup.py download
```

Alternatively, you can install HELICS in any way you like and point this package to the correct installation.
You can do this by setting the `PYHELICS_INSTALL` environment variable.
The path to the installation must be the root of the installation.

On Linux or Mac, add the following to your `~/.bashrc`.

```
export PYHELICS_INSTALL="/path/to/helics_installation"
```

where

```bash
$ tree /path/to/helics_installation

helics_installation
├── include
│  └── helics
├── lib
│  ├── cmake
│  ├── libhelicsSharedLib.2.6.0.dylib
│  ├── libhelicsSharedLib.2.dylib -> libhelicsSharedLib.2.6.0.dylib
│  ├── libhelicsSharedLib.dylib -> libhelicsSharedLib.2.dylib
│  ├── libzmq.5.2.2.dylib
│  ├── libzmq.5.dylib -> libzmq.5.2.2.dylib
│  ├── libzmq.dylib -> libzmq.5.dylib
│  └── pkgconfig
└── share
   ├── doc
      ├── helics
         └── man
```


On Windows, follow instructions online to set a user environment variable to the path of the HELICS installation.

**Install**

Next, you can install pyhelics by either using `pip` or setting your `PYTHONPATH`

```
git clone https://github.com/GMLC-TDC/pyhelics
cd pyhelics
python -m pip install -e .
```

This will install `pyhelics`.

Run the following to ensure that everything is working as expected.

```ipython
import helics as h
print(h.__file__) # this should print the path to the __init__.py file in the pyhelics repository
print(h.helicsGetVersion()) # this should print the version of the HELICS library in the PYHELICS_INSTALL environment or the latest version of HELICS
```

See [Migration from HELICS2 to HELICS3](./migration-helics2-helics3.md) for more information on changes between this version and the SWIG version of the HELICS library.

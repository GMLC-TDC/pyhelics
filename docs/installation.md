# Installation

This package uses `cffi` to interface with the HELICS library.
The source for this package contains only pure python code.

Python helics packages with version numbers greater than `v2.6.0` use this new cffi interface.
Versions equal to and prior to `v2.6.0` used swig to generate the Python API.

## Install from PyPI (recommended)

```bash
$ which python # sanity check on Unix
$ which pip    # sanity check on Unix

$ where python # sanity check on Windows
$ where pip    # sanity check on Windows

$ python -m pip install 'helics[cli]'
```

Using `python -m pip` invokes the `pip` module from the `python` process. This is the safest way to ensure you are installing `helics` into the place `python` will look for packages.
If `pip` and `python` belong to the same environment, you can invoke `pip` directly.

It is recommended to use the optional `[cli]` extension on the PyHELICS install to provide the use of the "runner" functionality for launching co-simulations (among other features) All of the [HELICS User Guide examples](https://docs.helics.org/en/latest/user-guide/examples/examples_index.html) use the runner.

This will give you the latest version of the python helics interface.
If you already have helics installed, you can upgrade to the latest version by using the following:

```bash
$ pip install helics --upgrade
```

You can install a specific version by using the following:

```bash
$ pip install helics
```

By default, when you install from PyPI, the version number of the package will match the version of HELICS that is installed.
For example, if you run the following:

```bash
$ pip install helics
```

You will also get precompiled binaries of [HELICS](https://github.com/GMLC-TDC/HELICS/releases/latest) for your platform if they exist.
If they don't exist, a source distribution will be installed in which case the user must provide the location of the binaries.
See the next section for more information about how to do that.

### Custom version of HELICS

The python package in this repository uses a environment variable called `PYHELICS_INSTALL` to choose the location of the precompiled binaries of the C HELICS library.
If you wish to change the version of HELICS used, you can set this environment variable to point to the location of an HELICS installation.

For example, let's say as a user you want to use HELICS in a Conda environment.

```bash
$ conda create -n helics-py3-env python=3 -y
$ conda activate helics-py3-env
```

Running `import helics` in python in this environment throws an error because python package hasn't been installed yet.

```bash
$ python -c 'import helics'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  ModuleNotFoundError: No module named 'helics'
```

You can install `helics` using `pip`.

```bash
$ pip install helics
pip install helics
Collecting helics
  Downloading helics-2.6.1.post0-py3-none-macosx_10_9_x86_64.whl (6.6 MB)
     |████████████████████████████████| 6.6 MB 2.3 MB/s
Collecting enum34>=1.1.10
  Using cached enum34-1.1.10-py3-none-any.whl (11 kB)
Collecting cffi>=1.0.0
  Using cached cffi-1.14.3-2-cp38-cp38-macosx_10_9_x86_64.whl (176 kB)
Collecting pycparser
  Using cached pycparser-2.20-py2.py3-none-any.whl (112 kB)
Installing collected packages: enum34, pycparser, cffi, helics
Successfully installed cffi-1.14.3 enum34-1.1.10 helics-2.6.1.post0 pycparser-2.20
```

Now that you have installed the python package, you can check that it works:

```bash
$ python -c "import helics; print(helics.helicsGetVersion())"
2.6.1 (2020-10-15)
```

This installs the Python package `helics-2.6.1.post0` and it comes with precompiled binaries for HELICS version 2.6.1 that we released on 2020-10-15.

Let's say you've made modification to the HELICS library or compiled it with some different flags.
Or you are interested in a using an older version of HELICS.
You can do that with this python package by changing the `PYHELICS_INSTALL` environment variable.

As an example, if you want to use the Python package with HELICS v2.5.2, you can clone the git repository for HELICS, build from source and install it to any location.
In this example, I chose to install it in `~/local/helics-v2.5.2`.

```bash
$ git clone https://github.com/GMLC-TDC/HELICS
$ cd HELICS
$ git checkout v2.5.2
$ mkdir -p build
$ cmake -DCMAKE_INSTALL_PREFIX=~/local/helics-v2.5.2 ..
$ make -j8 && make install
```

Now in bash, you can set the environment variable:

```bash
$ export PYHELICS_INSTALL=~/local/helics-v2.5.2
```

Now when you `import helics` and print the version you'll get `2.5.2 (2020-06-14)`.

```bash
$ python -c "import helics; print(helics.helicsGetVersion())"
2.5.2 (2020-06-14)
```

If you want to build from source and use the `develop` branch:

```bash
$ git checkout develop
$ git submodule update
$ cmake -DCMAKE_INSTALL_PREFIX=~/local/helics-develop ..
$ make -j8 && make install
$ export PYHELICS_INSTALL=~/local/helics-develop
$ python -c "import helics; print(helics.helicsGetVersion())"
2.6.0-develop-g3a460f1f (2020-09-24)
```

The Python HELICS cffi interface is tested with the latest version of HELICS.
If you find any issues with earlier versions of HELICS, please report them on <https://github.com/GMLC-TDC/HELICS/issues>.

## From Source

### Download

In order to run this package, you will need to download HELICS.

You can use this package to download HELICS.

```bash
$ git clone https://github.com/GMLC-TDC/pyhelics
$ cd pyhelics
$ python setup.py download
```

Alternatively, you can install HELICS in any way you like and point this package to the correct installation.
You can do this by setting the `PYHELICS_INSTALL` environment variable, as described in the previous section.
The path to the installation must be the root of the installation.

On Linux or Mac, add the following to your `~/.bashrc`.

```bash
$ export PYHELICS_INSTALL="/path/to/helics_installation"
```

where

```bash
$ tree /path/to/helics_installation

helics_installation
├── include
│ └── helics
├── lib
│ ├── cmake
│ ├── libhelicsSharedLib.2.6.1.dylib
│ ├── libhelicsSharedLib.2.dylib - > libhelicsSharedLib.2.6.1.dylib
│ ├── libhelicsSharedLib.dylib - > libhelicsSharedLib.2.dylib
│ ├── libzmq.5.2.2.dylib
│ ├── libzmq.5.dylib - > libzmq.5.2.2.dylib
│ ├── libzmq.dylib - > libzmq.5.dylib
│ └── pkgconfig
└── share
├── doc
├── helics
└── man
```

On Windows, follow instructions online to set a user environment variable to the path of the HELICS installation.
You can also use `set PYHELICS_INSTALL="C:\path\to\helics_installation"` in a command line session.

### Install

Next, you can install pyhelics by either using `pip` or setting your `PYTHONPATH`

```bash
$ git clone https://github.com/GMLC-TDC/pyhelics
$ cd pyhelics
$ python -m pip install -e .
```

This will install `pyhelics`.

Run the following to ensure that everything is working as expected.

```ipython
import helics as h
print(h.__file__) # this should print the path to the __init__.py file in the pyhelics repository
print(h.helicsGetVersion()) # this should print the version of the HELICS library in the PYHELICS_INSTALL environment or the latest version of HELICS
```

See [Migration from HELICS2 to HELICS3](./migration-helics2-helics3.md) for more information on changes between this version and the SWIG version of the HELICS library.

### Linking HELICS library

If you are interested in using the HELICS libraries that are installed along with Python with another application, you can find them in the location that is printed by running the following:

```bash
$ python -c 'import helics as h; print(h._build.PYHELICS_INSTALL)'
```

### Additional environment variables

- `PYHELICS_FREE_ON_DESTRUCTION` (True): Calls `helicsFederateFree` on `HelicsFederate` destruction, and similar respective functions for other objects.
- `PYHELICS_CLEANUP_ON_DESTRUCTION` (False): Calls `helicsCleanup` on `HelicsFederate` and other objects destruction.

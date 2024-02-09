#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

import re
import sys
import os
import struct
import shutil
import platform
import tarfile
import zipfile
import subprocess
import shlex

from setuptools import setup, Extension, Command
from setuptools.dist import Distribution
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist

from wheel.bdist_wheel import bdist_wheel
from distutils.dir_util import copy_tree
from distutils import log

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


HERE = os.path.dirname(os.path.abspath(__file__))
IS_REPO = os.path.exists(os.path.join(HERE, ".git"))
STATIC_DIR = os.path.join(HERE, "helics", "static")
NODE_ROOT = os.path.join(HERE, "client")
NPM_PATH = os.pathsep.join(
    [
        os.path.join(NODE_ROOT, "node_modules", ".bin"),
        os.environ.get("PATH", os.defpath),
    ]
)


def update_package_data(distribution):
    """update package_data to catch changes during setup"""
    build_py = distribution.get_command_obj("build_py")
    # distribution.package_data = find_package_data()
    # re-init build_py options which load package_data
    build_py.finalize_options()


def js_prerelease(command, strict=False):
    """decorator for building minified js/css prior to another command"""

    class DecoratedCommand(command):
        def run(self):
            jsdeps = self.distribution.get_command_obj("jsdeps")
            if not IS_REPO and all(os.path.exists(t) for t in jsdeps.targets):
                # sdist, nothing to do
                command.run(self)
                return

            try:
                self.distribution.run_command("jsdeps")
            except Exception as e:
                missing = [t for t in jsdeps.targets if not os.path.exists(t)]
                if strict or missing:
                    log.warn("rebuilding js and css failed")
                    if missing:
                        log.error("missing files: %s" % missing)
                    raise e
                else:
                    log.warn("rebuilding js and css failed (not a problem)")
                    log.warn(str(e))
            command.run(self)
            update_package_data(self.distribution)

    return DecoratedCommand


class NPM(Command):
    description = "install package.json dependencies using npm"

    user_options = []

    node_modules = os.path.join(NODE_ROOT, "node_modules")

    targets = ["index.html"]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def get_npm_name(self):
        npm_name = "npm"
        if platform.system() == "Windows":
            npm_name = "npm.cmd"
        return npm_name

    def has_npm(self):
        npm_name = self.get_npm_name()
        try:
            subprocess.check_call([npm_name, "--version"])
            return True
        except:
            return False

    def should_run_npm_install(self):
        node_modules_exists = os.path.exists(self.node_modules)
        return self.has_npm() and not node_modules_exists

    def run(self):
        has_npm = self.has_npm()
        if not has_npm:
            log.error("`npm` unavailable, skipping npm build.  If you're running this command using " "sudo, make sure `npm` is available to sudo")
            return

        env = os.environ.copy()
        env["PATH"] = NPM_PATH

        npm_name = self.get_npm_name()

        if self.should_run_npm_install():
            log.info("Installing build dependencies with npm.  " "This may take a while...")
            subprocess.check_call(
                [npm_name, "install"],
                cwd=NODE_ROOT,
                stdout=sys.stdout,
                stderr=sys.stderr,
            )
            os.utime(self.node_modules, None)

        subprocess.check_call(
            [npm_name, "run", "build"],
            cwd=NODE_ROOT,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

        copy_tree(os.path.join(NODE_ROOT, "build"), os.path.join(STATIC_DIR))

        for t in self.targets:
            if not os.path.exists(os.path.join(STATIC_DIR, t)):
                msg = "Missing file: %s" % t
                if not has_npm:
                    msg += "\nnpm is required to build a development version "
                    "of a widget extension"
                raise ValueError(msg)

        # update package data in case this created new files
        update_package_data(self.distribution)


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


PYHELICS_VERSION = read(os.path.join(os.path.dirname(__file__), "helics", "_version.py"), encoding="utf-8")
PYHELICS_VERSION = PYHELICS_VERSION.splitlines()[1].split()[2].strip('"').strip("'").lstrip("v")

HELICS_VERSION = re.findall(r"(?:(\d+\.(?:\d+\.)*\d+))", PYHELICS_VERSION)[0]
# HELICS_VERSION = "{}-beta".format(HELICS_VERSION)

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

HELICS_SOURCE = os.path.join(CURRENT_DIRECTORY, "./_source")
PYHELICS_INSTALL = os.environ.get("PYHELICS_INSTALL", os.path.join(CURRENT_DIRECTORY, "./helics/install"))

DOWNLOAD_URL = "https://github.com/GMLC-TDC/HELICS/releases/download/v{version}/Helics-v{version}-source.tar.gz".format(version=HELICS_VERSION)


def create_default_url(helics_version, plat_name=""):
    if "macos" in plat_name.lower():
        if helics_version.startswith("3") and int(helics_version.split(".")[1]) >= 1:  # >= 3.1.x
            default_url = (
                "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-macOS-universal2.zip".format(
                    helics_version=helics_version
                )
            )
        else:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-macOS-x86_64.zip".format(
                helics_version=helics_version
            )
    elif "win" in plat_name.lower():
        if "win32" in plat_name.lower():
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-win32.zip".format(
                helics_version=helics_version
            )
        else:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-win64.zip".format(
                helics_version=helics_version
            )

    elif "linux" in plat_name.lower():
        default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-Linux-x86_64.tar.gz".format(
            helics_version=helics_version
        )
    elif platform.system() == "Darwin":
        if helics_version.startswith("3") and int(helics_version.split(".")[1]) >= 1:  # >= 3.1.x
            default_url = (
                "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-macOS-universal2.zip".format(
                    helics_version=helics_version
                )
            )
        else:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-macOS-x86_64.zip".format(
                helics_version=helics_version
            )
    elif platform.system() == "Windows":
        if struct.calcsize("P") * 8 == 32:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-win32.zip".format(
                helics_version=helics_version
            )
        else:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-win64.zip".format(
                helics_version=helics_version
            )

    elif platform.system() == "Linux":
        default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-{helics_version}-Linux-x86_64.tar.gz".format(
            helics_version=helics_version
        )
    else:
        raise NotImplementedError("Unsupported platform {}".format(platform.system()))

    return default_url


def _is_symlink(file_info):
    """
    Check the upper 4 bits of the external attribute for a symlink.
    See: https://unix.stackexchange.com/questions/14705/the-zip-formats-external-file-attribute
    Parameters
    ----------
    file_info : zipfile.ZipInfo
        The ZipInfo for a ZipFile
    Returns
    -------
    bool
        A response regarding whether the ZipInfo defines a symlink or not.
    """

    return (file_info.external_attr >> 28) == 0xA


def _extract(file_info, output_dir, zip_ref):
    """
    Unzip the given file into the given directory while preserving file permissions in the process.
    Parameters
    ----------
    file_info : zipfile.ZipInfo
        The ZipInfo for a ZipFile
    output_dir : str
        Path to the directory where the it should be unzipped to
    zip_ref : zipfile.ZipFile
        The ZipFile we are working with.
    Returns
    -------
    string
        Returns the target path the Zip Entry was extracted to.
    """

    # Handle any regular file/directory entries
    if not _is_symlink(file_info):
        return zip_ref.extract(file_info, output_dir)

    source = zip_ref.read(file_info.filename).decode("utf8")
    link_name = os.path.normpath(os.path.join(output_dir, file_info.filename))

    # make leading dirs if needed
    leading_dirs = os.path.dirname(link_name)
    if not os.path.exists(leading_dirs):
        os.makedirs(leading_dirs)

    # If the link already exists, delete it or symlink() fails
    if os.path.lexists(link_name):
        os.remove(link_name)

    # Create a symbolic link pointing to source named link_name.
    os.symlink(source, link_name)

    return link_name


def _set_permissions(zip_file_info, extracted_path):
    """
    Sets permissions on the extracted file by reading the ``external_attr`` property of given file info.
    Parameters
    ----------
    zip_file_info : zipfile.ZipInfo
        Object containing information about a file within a zip archive
    extracted_path : str
        Path where the file has been extracted to
    """

    # Permission information is stored in first two bytes.
    permission = zip_file_info.external_attr >> 16
    if not permission:
        return

    os.chmod(extracted_path, permission)


def _override_permissions(path, permission):
    """
    Forcefully override the permissions on the path
    Parameters
    ----------
    path str
        Path where the file or directory
    permission octal int
        Permission to set
    """
    if permission:
        os.chmod(path, permission)


def unzip(zip_file_path, output_dir, permission=None):
    """
    Unzip the given file into the given directory while preserving file permissions in the process.
    Parameters
    ----------
    zip_file_path : str
        Path to the zip file
    output_dir : str
        Path to the directory where the it should be unzipped to
    permission : int
        Permission to set in an octal int form
    """
    extracted_path = None
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:

        # For each item in the zip file, extract the file and set permissions if available
        for file_info in zip_ref.infolist():
            extracted_path = _extract(file_info, output_dir, zip_ref)

            # If the extracted_path is a symlink, do not set the permissions. If the target of the symlink does not
            # exist, then os.chmod will fail with FileNotFoundError
            if not os.path.islink(extracted_path):
                _set_permissions(file_info, extracted_path)
                _override_permissions(extracted_path, permission)

    if extracted_path is not None and not os.path.islink(extracted_path):
        _override_permissions(output_dir, permission)


class HELICSDownloadCommand(Command):
    description = "Download helics libraries dependency"
    user_options = [
        ("pyhelics-install=", None, "path to pyhelics install folder"),
        ("plat-name=", None, "platform name to embed in generated filenames"),
    ]

    def initialize_options(self):
        self.plat_name = ""
        self.pyhelics_install = os.path.join(CURRENT_DIRECTORY, "./helics/install")
        if os.path.exists(self.pyhelics_install):
            shutil.rmtree(self.pyhelics_install)

    def finalize_options(self):
        pass

    def run(self):
        self.helics_url = create_default_url(HELICS_VERSION, self.plat_name)
        print("Downloading {}".format(self.helics_url))
        r = urlopen(self.helics_url)
        if r.getcode() == 200:
            if self.helics_url.endswith(".zip"):
                with open("./tmp.zip", "wb") as f:
                    f.write(r.read())
                unzip("./tmp.zip", self.pyhelics_install)
                os.remove("./tmp.zip")

                if len(os.listdir(self.pyhelics_install)) == 1 and os.listdir(self.pyhelics_install)[0].startswith("Helics-"):
                    tmp = os.listdir(self.pyhelics_install)[0]
                    for folder in os.listdir(os.path.join(self.pyhelics_install, tmp)):
                        p = Path(os.path.join(self.pyhelics_install, tmp, folder)).absolute()
                        parent_dir = p.parents[1]
                        p.rename(parent_dir / p.name)
            else:
                content = io.BytesIO(r.read())
                content.seek(0)
                with tarfile.open(fileobj=content) as tf:
                    dirname = tf.getnames()[0].partition("/")[0]
                    tf.extractall()
                shutil.move(dirname, self.pyhelics_install)
            for file in os.listdir(os.path.join(self.pyhelics_install, "bin")):
                f = Path(os.path.join(self.pyhelics_install, "bin", file))
                try:
                    import stat

                    f.chmod(f.stat().st_mode | stat.S_IEXEC)
                except:
                    pass
            files = [
                "helics_api.h",
                "helics_enums.h",
                os.path.join("shared_api_library", "api-data.h"),
                os.path.join("shared_api_library", "helics.h"),
                os.path.join("shared_api_library", "helics_export.h"),
                os.path.join("shared_api_library", "MessageFederate.h"),
                os.path.join("shared_api_library", "MessageFilters.h"),
                os.path.join("shared_api_library", "ValueFederate.h"),
                os.path.join("shared_api_library", "helicsCallbacks.h"),
            ]
            IGNOREBLOCK = False
            print("Writing to {}".format(os.path.abspath(self.pyhelics_install)))
            for file in files:
                if not os.path.isfile(os.path.join(self.pyhelics_install, "include", "helics", file)):
                    continue
                with open(os.path.join(self.pyhelics_install, "include", "helics", file)) as f:
                    lines = []
                    for line in f:
                        if line.startswith("#ifdef __cplusplus"):
                            IGNOREBLOCK = True
                            continue
                        if IGNOREBLOCK is True and line.startswith("#endif"):
                            IGNOREBLOCK = False
                            continue
                        if IGNOREBLOCK is True:
                            continue
                        if line.startswith("#"):
                            continue
                        lines.append(line)
                    data = "\n".join(lines)
                    data = data.replace("HELICS_EXPORT", "")
                    data = data.replace("HELICS_DEPRECATED_EXPORT", "")
                with open(os.path.join(self.pyhelics_install, "include", "helics", file), "w") as f:
                    f.write(data)


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=HELICS_SOURCE):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = sourcedir


class HELICSCMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(["cmake", "--version"])
            cmake_version = re.search(r"version\s*([\d.]+)", out.decode().lower()).group(1)
            cmake_version = [int(i) for i in cmake_version.split(".")]
            if cmake_version < [3, 5, 1]:
                raise RuntimeError("CMake >= 3.5.1 is required to build helics")

        except OSError:
            if not os.path.exists(PYHELICS_INSTALL):
                raise RuntimeError("CMake must be installed to build the following extensions: " + ", ".join(e.name for e in self.extensions))

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        self.helics_url = DOWNLOAD_URL
        self.helics_source = HELICS_SOURCE
        if not os.path.exists(PYHELICS_INSTALL):
            r = urlopen(self.helics_url)
            if r.getcode() == 200:
                content = io.BytesIO(r.read())
                content.seek(0)
                with tarfile.open(fileobj=content) as tf:
                    tf.extractall(self.helics_source)
        else:
            return

        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        extdir = os.path.join(extdir, "helics", "install")
        # required for auto - detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cmake_args = [
            "-DHELICS_DISABLE_GIT_OPERATIONS=OFF",
            "-DHELICS_ZMQ_FORCE_SUBPROJECT=ON",
            "-DHELICS_ZMQ_SUBPROJECT=ON",
            "-DHELICS_DISABLE_BOOST=ON",
            "-DCMAKE_BUILD_TYPE=Release",
            "-DCMAKE_INSTALL_PREFIX={}".format(extdir),
        ]

        cfg = "Debug" if self.debug else "Release"
        build_args = ["--config", cfg]

        if platform.system() == "Windows":
            cmake_args += ["-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}".format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ["-A", "x64"]
                build_args += ["--", "/m"]
        else:
            cmake_args += ["-DCMAKE_BUILD_TYPE=" + cfg]
            build_args += ["--", "-j"]

        env = os.environ.copy()
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        cmd = " ".join(["cmake", "--build", ".", "--target", "install"] + build_args)
        print(cmd)
        subprocess.check_call(shlex.split(cmd), cwd=self.build_temp)

        files = [
            "helics_api.h",
            "helics_enums.h",
            os.path.join("shared_api_library", "api-data.h"),
            os.path.join("shared_api_library", "helics.h"),
            os.path.join("shared_api_library", "helics_export.h"),
            os.path.join("shared_api_library", "MessageFederate.h"),
            os.path.join("shared_api_library", "MessageFilters.h"),
            os.path.join("shared_api_library", "ValueFederate.h"),
            os.path.join("shared_api_library", "helicsCallbacks.h"),
        ]
        IGNOREBLOCK = False
        for file in files:
            if not os.path.isfile(os.path.join(extdir, "include", "helics", file)):
                continue
            with open(os.path.join(extdir, "include", "helics", file)) as f:
                lines = []
                for line in f:
                    if line.startswith("#ifdef __cplusplus"):
                        IGNOREBLOCK = True
                        continue
                    if IGNOREBLOCK is True and line.startswith("#endif"):
                        IGNOREBLOCK = False
                        continue
                    if IGNOREBLOCK is True:
                        continue
                    if line.startswith("#"):
                        continue
                    lines.append(line)
                data = "\n".join(lines)
                data = data.replace("HELICS_EXPORT", "")
                data = data.replace("HELICS_DEPRECATED_EXPORT", "")
            with open(os.path.join(extdir, "include", "helics", file), "w") as f:
                f.write(data)


install_requires = ["cffi>=1.6.0", "strip-hints", "click>=8"]

if sys.version_info < (3, 4):
    install_requires.append("enum34")


class HelicsBdistWheel(bdist_wheel):
    def get_tag(self):
        rv = bdist_wheel.get_tag(self)
        return ("py3", "none") + rv[2:]


cmdclass = {
    "download": HELICSDownloadCommand,
    "build_ext": js_prerelease(HELICSCMakeBuild),
    "bdist_wheel": js_prerelease(HelicsBdistWheel),
    "develop": js_prerelease(develop),
    "build_py": js_prerelease(build_py),
    "egg_info": js_prerelease(egg_info),
    "sdist": js_prerelease(sdist, strict=True),
    "jsdeps": NPM,
}


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


helics_cli_install_requires = ["flask>=2", "requests", "flask-restful", "flask-cors", "pandas", "SQLAlchemy", "matplotlib"]

setup(
    name="helics",
    version=PYHELICS_VERSION,
    license="MIT",
    description="Python HELICS bindings",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Dheepak Krishnamurthy",
    author_email="me@kdheepak.com",
    url="https://github.com/GMLC-TDC/pyhelics",
    packages=["helics"],
    distclass=BinaryDistribution,
    py_modules=[splitext(basename(path))[0] for path in glob("helics/*.py")],
    # data_files=[("helics", ["install/include/helics/chelics.h"])],
    # cffi_modules=['helics/helics_build.py:ffibuilder'],
    package_data={"helics": ["install/*"]},
    ext_modules=[CMakeExtension("helics")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    project_urls={"Issue Tracker": "https://github.com/GMLC-TDC/pyhelics/issues"},
    keywords=["helics", "co-simulation"],
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={
        "cli": install_requires + helics_cli_install_requires,
        "tests": ["pytest", "pytest-ordering", "pytest-cov", "pytest-runner"],
        "docs": [
            "mkdocs",
            "inari[mkdocs]",
            "mkdocs-material",
            "black",
            "pygments",
            "pymdown-extensions",
        ],
    },
    cmdclass=cmdclass,
    entry_points={
        "console_scripts": [
            "helics=helics.cli:cli",
            "helics-cli=helics.cli:cli",
            "helics_app=helics.bin:helics_app",
            "helics_broker=helics.bin:helics_broker",
            "helics_broker_server=helics.bin:helics_broker_server",
            "helics_player=helics.bin:helics_player",
            "helics_recorder=helics.bin:helics_recorder",
        ]
    },
)

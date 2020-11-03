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

from setuptools import setup, Command
from setuptools.dist import Distribution

import re
import sys
import os
import platform
import tarfile
import shutil
import struct

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


PYHELICS_VERSION = read(os.path.join(os.path.dirname(__file__), "helics", "_version.py"), encoding="utf-8")
PYHELICS_VERSION = PYHELICS_VERSION.splitlines()[1].split()[2].strip('"').strip("'").lstrip("v")


HELICS_VERSION = re.findall(r"(?:(\d+\.(?:\d+\.)*\d+))", PYHELICS_VERSION)[0]

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def create_default_url():
    if platform.system() == "Darwin":
        default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-shared-{helics_version}-macOS-x86_64.tar.gz".format(
            helics_version=HELICS_VERSION
        )
    elif platform.system() == "Windows":
        if struct.calcsize("P") * 8 == 32:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-shared-{helics_version}-win32.tar.gz".format(
                helics_version=HELICS_VERSION
            )
        else:
            default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-shared-{helics_version}-win64.tar.gz".format(
                helics_version=HELICS_VERSION
            )

    elif platform.system() == "Linux":
        default_url = "https://github.com/GMLC-TDC/HELICS/releases/download/v{helics_version}/Helics-shared-{helics_version}-Linux-x86_64.tar.gz".format(
            helics_version=HELICS_VERSION
        )
    else:
        raise NotImplementedError("Unsupported platform {}".format(platform.system()))

    return default_url


class HELICSDownloadCommand(Command):
    description = "Download helics libraries dependency"
    user_options = [
        ("pyhelics-install=", None, "path to pyhelics install folder"),
    ]

    def initialize_options(self):
        self.helics_url = create_default_url()
        self.pyhelics_install = os.path.join(CURRENT_DIRECTORY, "./helics/install")
        if os.path.exists(self.pyhelics_install):
            shutil.rmtree(self.pyhelics_install)

    def finalize_options(self):
        pass

    def run(self):
        r = urlopen(self.helics_url)
        if r.getcode() == 200:
            content = io.BytesIO(r.read())
            content.seek(0)
            with tarfile.open(fileobj=content) as tf:
                dirname = tf.getnames()[0].partition("/")[0]
                tf.extractall()
            shutil.move(dirname, self.pyhelics_install)
            if platform.system() == "Linux":
                shutil.move(os.path.join(self.pyhelics_install, "lib64"), os.path.join(self.pyhelics_install, "lib"))


install_requires = ["cffi>=1.0.0", "strip-hints"]

if sys.version_info < (3, 4):
    install_requires.append("enum34")

setup(
    name="helics",
    version=PYHELICS_VERSION,
    license="MIT",
    description="Python HELICS bindings",
    long_description=read("README.md"),
    author="Dheepak Krishnamurthy",
    author_email="me@kdheepak.com",
    url="https://github.com/GMLC-TDC/pyhelics",
    packages=["helics"],
    py_modules=[splitext(basename(path))[0] for path in glob("helics/*.py")],
    # data_files=[("helics", ["install/include/helics/chelics.h"])],
    package_data={"helics": ["install/*"]},
    distclass=BinaryDistribution,
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
        "Programming Language :: Python :: 2.7",
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
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*",
    install_requires=install_requires,
    extras_require={
        "tests": ["pytest", "pytest-ordering", "pytest-cov", "pytest-runner"],
        "docs": ["mkdocs", "inari[mkdocs]", "mkdocs-material", "black", "pygments", "pymdown-extensions"],
    },
    cmdclass={"download": HELICSDownloadCommand},
)

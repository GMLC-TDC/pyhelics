# -*- coding: utf-8 -*-
from .capi import *
from ._version import __version__

import atexit

atexit.register(helicsCloseLibrary)

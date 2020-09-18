# -*- coding: utf-8 -*-
__version__ = "v2.6.0.post0.dev0"
from .capi import *

import atexit

atexit.register(helicsCloseLibrary)

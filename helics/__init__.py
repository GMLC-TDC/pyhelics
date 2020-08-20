# -*- coding: utf-8 -*-
from .capi import *

import atexit

atexit.register(helicsCloseLibrary)

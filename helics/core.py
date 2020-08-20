# -*- coding: utf-8 -*-
from . import capi as h
import logging

from typing import List, Any, TypeVar

Core = TypeVar("Any")


class Core:
    def __init__(self, core=None, clone=False):
        if core is not None and type(core) == Core and clone is True:
            self._core = h.helicsCoreClone(core._core)
        elif core is not None and type(core) == Core and clone is False:
            self._core = core._core
        elif core is not None:
            self._core = core

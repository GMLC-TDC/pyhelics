# -*- coding: utf-8 -*-

import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import helics as h


def test_helicsGetVersion():
    print(h.helicsGetVersion())
    try:
        assert h.helicsGetVersion().startswith("2")
    except Exception:
        assert h.helicsGetVersion().startswith("3")

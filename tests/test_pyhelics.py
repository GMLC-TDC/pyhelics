# -*- coding: utf-8 -*-

import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import helics as h


def test_helicsGetVersion():
    assert h.helicsGetVersion() == "3.0.0-alpha.1 (2020-09-24)"

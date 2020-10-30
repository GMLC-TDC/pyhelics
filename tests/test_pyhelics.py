# -*- coding: utf-8 -*-

import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import helics as h


def test_helicsGetVersion():
    assert h.helicsGetVersion() == "2.6.1 (2020-10-15)"

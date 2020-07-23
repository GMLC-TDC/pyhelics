# -*- coding: utf-8 -*-

from helics import helicsGetVersion


def test_helicsGetVersion():
    assert helicsGetVersion() == "v2.5.0"

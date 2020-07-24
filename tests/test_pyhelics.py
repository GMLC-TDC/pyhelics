# -*- coding: utf-8 -*-

import helics as h


def test_helicsGetVersion():
    assert h.helicsGetVersion() == "2.5.2 (2020-06-14)"

# -*- coding: utf-8 -*-

import helics as h


def test_helicsGetVersion():
    print(h.helicsGetVersion())
    try:
        assert h.helicsGetVersion().startswith("2")
    except Exception:
        assert h.helicsGetVersion().startswith("3")

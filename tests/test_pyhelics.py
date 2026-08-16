# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause


import helics as h


def test_helicsGetVersion():
    print(h.helicsGetVersion())
    try:
        assert h.helicsGetVersion().startswith("2")
    except Exception:
        assert h.helicsGetVersion().startswith("3")

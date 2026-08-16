# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause

import pytest
import helics as h


@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()

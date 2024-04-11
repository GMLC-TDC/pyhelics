# -*- coding: utf-8 -*-
import pytest
import helics as h


@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()
    h.helicsCloseLibrary()

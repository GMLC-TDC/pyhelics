# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause

import helics as h


def test_data_buffer_scalar_round_trips():
    buffer = h.helicsCreateDataBuffer(64)
    assert h.helicsDataBufferIsValid(buffer)
    assert h.helicsDataBufferReserve(buffer, 128)
    assert h.helicsDataBufferCapacity(buffer) >= 128

    h.helicsDataBufferFillFromInteger(buffer, 42)
    assert h.helicsDataBufferToInteger(buffer) == 42

    h.helicsDataBufferFillFromDouble(buffer, 3.5)
    assert h.helicsDataBufferToDouble(buffer) == 3.5

    h.helicsDataBufferFillFromBoolean(buffer, True)
    assert h.helicsDataBufferToBoolean(buffer) is True

    h.helicsDataBufferFillFromChar(buffer, "z")
    assert h.helicsDataBufferToChar(buffer) == "z"

    h.helicsDataBufferFillFromTime(buffer, 12.25)
    assert h.helicsDataBufferToTime(buffer) == 12.25


def test_data_buffer_string_and_raw_round_trips():
    buffer = h.helicsCreateDataBuffer(64)

    h.helicsDataBufferFillFromString(buffer, "hello")
    assert h.helicsDataBufferToString(buffer) == "hello"

    h.helicsDataBufferFillFromRawString(buffer, b"abc\x00def")
    assert h.helicsDataBufferToRawString(buffer) == b"abc\x00def"


def test_data_buffer_complex_vector_and_named_point_round_trips():
    buffer = h.helicsCreateDataBuffer(64)

    h.helicsDataBufferFillFromComplex(buffer, complex(1.25, -2.5))
    assert h.helicsDataBufferToComplex(buffer) == complex(1.25, -2.5)

    h.helicsDataBufferFillFromComplexObject(buffer, complex(-3.0, 4.5))
    assert h.helicsDataBufferToComplexObject(buffer) == complex(-3.0, 4.5)

    h.helicsDataBufferFillFromVector(buffer, [1.0, 2.0, 3.0])
    assert h.helicsDataBufferToVector(buffer) == [1.0, 2.0, 3.0]

    h.helicsDataBufferFillFromComplexVector(buffer, [complex(1, 2), complex(3, 4)])
    assert h.helicsDataBufferToComplexVector(buffer) == [complex(1, 2), complex(3, 4)]

    h.helicsDataBufferFillFromNamedPoint(buffer, "point", 8.0)
    assert h.helicsDataBufferToNamedPoint(buffer) == ("point", 8.0)

    clone = h.helicsDataBufferClone(buffer)
    assert h.helicsDataBufferToNamedPoint(clone) == ("point", 8.0)


def test_wrap_data_in_buffer_keeps_python_storage_alive():
    buffer = h.helicsWrapDataInBuffer(b"wrap", 16)
    assert h.helicsDataBufferData(buffer) == b"wrap"

# -*- coding: utf-8 -*-
import ast
from pathlib import Path


CAPI_PATH = Path(__file__).resolve().parents[1] / "helics" / "capi.py"


def _module():
    return ast.parse(CAPI_PATH.read_text(encoding="utf-8"))


def _function(name):
    for node in _module().body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError("missing function {}".format(name))


def _arg_names(node):
    return [arg.arg for arg in node.args.args]


def _loadsym_names(node):
    names = []
    for child in ast.walk(node):
        if (
            isinstance(child, ast.Call)
            and isinstance(child.func, ast.Name)
            and child.func.id == "loadSym"
            and child.args
            and isinstance(child.args[0], ast.Constant)
        ):
            names.append(child.args[0].value)
    return names


def _f_calls(node):
    return [
        child
        for child in ast.walk(node)
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name) and child.func.id == "f"
    ]


def _uses_data_handle(node):
    return any(
        isinstance(child, ast.Attribute)
        and child.attr == "handle"
        and isinstance(child.value, ast.Name)
        and child.value.id == "data"
        for child in ast.walk(node)
    )


def _uses_handle(node, arg_name):
    return any(
        isinstance(child, ast.Attribute)
        and child.attr == "handle"
        and isinstance(child.value, ast.Name)
        and child.value.id == arg_name
        for child in ast.walk(node)
    )


def _raises_not_implemented(node):
    return any(
        isinstance(child, ast.Raise)
        and isinstance(child.exc, ast.Call)
        and isinstance(child.exc.func, ast.Name)
        and child.exc.func.id == "NotImplementedError"
        for child in ast.walk(node)
    )


def test_data_buffer_wrappers_load_matching_c_symbols():
    names = [
        "helicsDataBufferFree",
        "helicsDataBufferIsValid",
        "helicsDataBufferConvertToType",
        "helicsDataBufferClone",
        "helicsDataBufferCapacity",
        "helicsDataBufferSize",
        "helicsDataBufferStringSize",
        "helicsDataBufferToTime",
        "helicsDataBufferVectorSize",
        "helicsDataBufferToVector",
        "helicsDataBufferReserve",
        "helicsDataBufferData",
        "helicsDataBufferFillFromInteger",
        "helicsDataBufferFillFromDouble",
        "helicsDataBufferFillFromString",
        "helicsDataBufferFillFromRawString",
        "helicsDataBufferFillFromBoolean",
        "helicsDataBufferFillFromChar",
        "helicsDataBufferFillFromTime",
        "helicsDataBufferFillFromComplex",
        "helicsDataBufferFillFromComplexObject",
        "helicsDataBufferFillFromComplexVector",
        "helicsDataBufferFillFromVector",
        "helicsDataBufferFillFromNamedPoint",
        "helicsDataBufferType",
        "helicsDataBufferToInteger",
        "helicsDataBufferToChar",
        "helicsDataBufferToString",
        "helicsDataBufferToRawString",
        "helicsDataBufferToDouble",
        "helicsDataBufferToBoolean",
        "helicsDataBufferToComplex",
        "helicsDataBufferToComplexObject",
        "helicsDataBufferToComplexVector",
        "helicsDataBufferToNamedPoint",
    ]

    for name in names:
        node = _function(name)
        assert _loadsym_names(node) == [name]
        assert _uses_data_handle(node)
        assert not _raises_not_implemented(node)


def test_data_buffer_vector_wrappers_pass_lengths():
    expected = {
        "helicsDataBufferFillFromVector": ["data", "value"],
        "helicsDataBufferFillFromComplexVector": ["data", "value"],
    }

    for name, args in expected.items():
        node = _function(name)
        assert _arg_names(node) == args
        assert any(len(call.args) == 3 for call in _f_calls(node))


def test_data_buffer_string_wrappers_match_c_arg_counts():
    expected_call_lengths = {
        "helicsDataBufferToString": 4,
        "helicsDataBufferToRawString": 4,
        "helicsDataBufferToNamedPoint": 5,
    }

    for name, call_length in expected_call_lengths.items():
        node = _function(name)
        assert any(len(call.args) == call_length for call in _f_calls(node))


def test_wrappers_accepting_data_buffers_pass_handles():
    expected = {
        "helicsMessageSetDataBuffer": "data",
        "helicsPublicationPublishDataBuffer": "buffer",
    }

    for name, arg_name in expected.items():
        node = _function(name)
        assert name in _loadsym_names(node)
        assert _uses_handle(node, arg_name)

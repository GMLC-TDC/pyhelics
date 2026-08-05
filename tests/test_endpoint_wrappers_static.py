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


def _class(name):
    for node in _module().body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    raise AssertionError("missing class {}".format(name))


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


def _arg_names(node):
    return [arg.arg for arg in node.args.args]


def test_endpoint_wrappers_load_matching_c_symbols():
    expected = {
        "helicsEndpointSendBytesAt": ["endpoint", "data", "time"],
        "helicsEndpointRemoveTarget": ["endpoint", "target"],
    }

    for name, args in expected.items():
        node = _function(name)
        assert _arg_names(node) == args
        assert name in _loadsym_names(node)


def test_endpoint_handle_has_consistent_send_and_target_helpers():
    node = _class("HelicsEndpoint")
    methods = {child.name: child for child in node.body if isinstance(child, ast.FunctionDef)}

    assert {
        "add_source_target",
        "add_destination_target",
        "remove_target",
    } <= set(methods)

    send_data_calls = {
        child.func.id
        for child in ast.walk(methods["send_data"])
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name)
    }
    assert {
        "helicsEndpointSendBytes",
        "helicsEndpointSendBytesAt",
        "helicsEndpointSendBytesTo",
        "helicsEndpointSendBytesToAt",
    } <= send_data_calls

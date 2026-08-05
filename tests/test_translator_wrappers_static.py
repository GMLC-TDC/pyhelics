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


def test_translator_wrappers_load_matching_c_symbols():
    expected = {
        "helicsTranslatorSetString": ["translator", "property", "value"],
        "helicsTranslatorRemoveTarget": ["translator", "target"],
        "helicsTranslatorGetTag": ["translator", "tagname"],
        "helicsTranslatorSetTag": ["translator", "tagname", "tagvalue"],
    }

    for name, args in expected.items():
        node = _function(name)
        assert _arg_names(node) == args
        assert _loadsym_names(node) == [name]


def test_translator_handle_has_pythonic_helpers():
    node = _class("HelicsTranslator")
    method_names = {child.name for child in node.body if isinstance(child, ast.FunctionDef)}

    assert {
        "is_valid",
        "set",
        "set_string",
        "add_input_target",
        "add_publication_target",
        "add_source_endpoint",
        "add_destination_endpoint",
        "remove_target",
        "get_tag",
        "set_tag",
    } <= method_names

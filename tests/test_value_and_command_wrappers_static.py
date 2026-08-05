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


def _returns_handle(node):
    return ast.unparse(node.returns) if node.returns is not None else None


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


def _name_or_attr(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        return "{} {} {}".format(_name_or_attr(node.left), type(node.op).__name__, _name_or_attr(node.right))
    return type(node).__name__


def test_input_default_vector_wrappers_load_matching_c_symbols():
    for name in ("helicsInputSetDefaultVector", "helicsInputSetDefaultComplexVector"):
        node = _function(name)
        assert _arg_names(node) == ["ipt", "vectorInput"]
        assert _loadsym_names(node) == [name]


def test_input_default_complex_vector_passes_complex_count_to_c_api():
    node = _function("helicsInputSetDefaultComplexVector")
    calls = [
        child
        for child in ast.walk(node)
        if isinstance(child, ast.Call)
        and isinstance(child.func, ast.Name)
        and child.func.id == "f"
    ]

    assert len(calls) == 1
    assert len(calls[0].args) == 4
    assert _name_or_attr(calls[0].args[2]) == "vectorLength"


def test_command_wrappers_create_error_internally():
    expected = {
        "helicsCoreSendCommand": ["core", "target", "command"],
        "helicsCoreSendOrderedCommand": ["core", "target", "command"],
        "helicsBrokerSendCommand": ["broker", "target", "command"],
        "helicsBrokerSendOrderedCommand": ["broker", "target", "command"],
    }

    for name, args in expected.items():
        node = _function(name)
        assert _arg_names(node) == args
        assert _loadsym_names(node) == [name]


def test_input_registration_wrappers_advertise_input_handles():
    for name in (
        "helicsFederateRegisterInput",
        "helicsFederateRegisterTypeInput",
        "helicsFederateRegisterGlobalInput",
        "helicsFederateRegisterGlobalTypeInput",
    ):
        node = _function(name)
        assert _returns_handle(node) == "HelicsInput"
        assert "return HelicsInput(result)" in ast.unparse(node)

        docstring = ast.get_docstring(node)
        assert docstring is not None
        assert "**Returns**: `helics.HelicsInput`." in docstring
        assert "**Returns**: `helics.HelicsPublication`." not in docstring

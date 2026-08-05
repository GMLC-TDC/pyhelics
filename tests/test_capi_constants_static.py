# -*- coding: utf-8 -*-
import ast
from pathlib import Path


CAPI_PATH = Path(__file__).resolve().parents[1] / "helics" / "capi.py"


def _module():
    return ast.parse(CAPI_PATH.read_text(encoding="utf-8"))


def _class(name):
    for node in _module().body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    raise AssertionError("missing class {}".format(name))


def _class_constant(class_name, constant_name):
    for node in _class(class_name).body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == constant_name
        ):
            return _literal_value(node.value)
    raise AssertionError("missing {}.{}".format(class_name, constant_name))


def _literal_value(node):
    if isinstance(node, ast.Constant):
        return node.value
    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, ast.USub)
        and isinstance(node.operand, ast.Constant)
    ):
        return -node.operand.value
    raise AssertionError("unsupported literal node {}".format(type(node).__name__))


def _module_assignments(name):
    matches = []
    for node in _module().body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                matches.append(node.value)
    return matches


def _module_alias(name):
    assignments = _module_assignments(name)
    if len(assignments) != 1:
        raise AssertionError("expected one assignment for {}, got {}".format(name, len(assignments)))

    value = assignments[0]
    if (
        isinstance(value, ast.Attribute)
        and isinstance(value.value, ast.Name)
    ):
        return "{}.{}".format(value.value.id, value.attr)
    if isinstance(value, ast.Constant):
        return value.value
    raise AssertionError("unsupported assignment for {}".format(name))


def test_core_type_test_is_not_overwritten():
    assert _class_constant("HelicsCoreType", "TEST") == 3
    assert _module_alias("HELICS_CORE_TYPE_TEST") == "HelicsCoreType.TEST"


def test_current_data_type_constants():
    assert _class_constant("HelicsDataType", "UNKNOWN") == -1
    assert _class_constant("HelicsDataType", "CHAR") == 9
    assert _module_alias("HELICS_DATA_TYPE_UNKNOWN") == "HelicsDataType.UNKNOWN"
    assert _module_alias("HELICS_DATA_TYPE_CHAR") == "HelicsDataType.CHAR"


def test_current_error_constants():
    assert _class_constant("HelicsError", "USER_EXCEPTION") == -29
    assert _class_constant("HelicsError", "USER_ABORT") == 130
    assert _class_constant("HelicsError", "TERMINATED") == 143
    assert _module_alias("HELICS_ERROR_USER_ABORT") == "HelicsError.USER_ABORT"
    assert _module_alias("HELICS_ERROR_TERMINATED") == "HelicsError.TERMINATED"


def test_current_property_and_handle_option_constants():
    assert _class_constant("HelicsProperty", "INT_INDEX_GROUP") == 282
    assert _class_constant("HelicsProperty", "INT_VALUE_BUFFER_WARNING") == 283
    assert _class_constant("HelicsHandleOption", "TIME_RESTRICTED") == 557
    assert _module_alias("HELICS_PROPERTY_INT_INDEX_GROUP") == "HelicsProperty.INT_INDEX_GROUP"
    assert _module_alias("HELICS_PROPERTY_INT_VALUE_BUFFER_WARNING") == "HelicsProperty.INT_VALUE_BUFFER_WARNING"
    assert _module_alias("HELICS_HANDLE_OPTION_TIME_RESTRICTED") == "HelicsHandleOption.TIME_RESTRICTED"


def test_current_iteration_request_and_state_constants():
    assert _class_constant("HelicsIterationRequest", "HALT_OPERATIONS") == 5
    assert _class_constant("HelicsIterationRequest", "ERROR") == 7
    assert _class_constant("HelicsFederateState", "UNKNOWN") == -1
    assert _module_alias("HELICS_ITERATION_REQUEST_HALT_OPERATIONS") == "HelicsIterationRequest.HALT_OPERATIONS"
    assert _module_alias("HELICS_ITERATION_REQUEST_ERROR") == "HelicsIterationRequest.ERROR"
    assert _module_alias("HELICS_STATE_UNKNOWN") == "HelicsFederateState.UNKNOWN"

import ast
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from capi_api_test_utils import (
    arg_names,
    call_arg_exprs,
    c_api_enum_constants,
    c_api_prototypes,
    capi_functions,
    class_constant,
    class_constant_names,
    expr,
    f_calls,
    function_node,
    helics_api_header_path,
    load_symbols,
    module_alias,
    module_assignments,
    module_constant_values,
    raises_not_implemented,
)


DATA_BUFFER_WRAPPERS = [
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

DIRECT_C_CALL_WRAPPERS = [
    "helicsTranslatorSetString",
    "helicsTranslatorRemoveTarget",
    "helicsTranslatorGetTag",
    "helicsTranslatorSetTag",
    "helicsEndpointSendBytesAt",
    "helicsEndpointRemoveTarget",
    "helicsBrokerIsRoot",
    "helicsBrokerIsOpenToNewFederates",
    "helicsCoreIsOpenToNewFederates",
    "helicsMessageSetDataBuffer",
    "helicsPublicationPublishDataBuffer",
    "helicsInputSetDefaultVector",
    "helicsInputSetDefaultComplexVector",
    "helicsPublicationPublishVector",
    "helicsPublicationPublishComplexVector",
    "helicsFederateGetTag",
    "helicsMessageClear",
    "helicsMessageCopy",
    "helicsCoreSendCommand",
    "helicsCoreSendOrderedCommand",
    "helicsBrokerSendCommand",
    "helicsBrokerSendOrderedCommand",
    "helicsBrokerGlobalError",
    "helicsCoreGlobalError",
    "helicsQueryBufferFill",
] + DATA_BUFFER_WRAPPERS

HANDLE_ARGUMENTS = {
    "helicsMessageSetDataBuffer": ("data",),
    "helicsPublicationPublishDataBuffer": ("buffer",),
    "helicsMessageCopy": ("source_message", "destination_message"),
    "helicsQueryBufferFill": ("buffer",),
}
for _name in DATA_BUFFER_WRAPPERS:
    HANDLE_ARGUMENTS[_name] = ("data",)

COMPLEX_VECTOR_COUNT_ARGS = {
    "helicsInputSetDefaultComplexVector": "vectorLength",
    "helicsPublicationPublishComplexVector": "vectorLength",
    "helicsDataBufferFillFromComplexVector": "vector_length",
}

INTERNAL_HELICS_CONSTANTS_OMITTED_FROM_PYHELICS = {
    "HELICS_ITERATION_REQUEST_HALT_OPERATIONS",
    "HELICS_ITERATION_REQUEST_ERROR",
}

INTENTIONAL_PYHELICS_CONSTANT_OVERRIDES = {
    "HELICS_CORE_TYPE_TEST": "pyHELICS uses ZMQ as its test core alias",
}

DEPRECATED_C_EXPORTS_OMITTED_FROM_PYHELICS = {
    "helicsEndpointClearMessages",
    "helicsSubscriptionGetTarget",
}


@pytest.fixture(scope="module")
def c_api_header():
    try:
        return helics_api_header_path()
    except FileNotFoundError as exc:
        pytest.skip(str(exc))


@pytest.fixture(scope="module")
def c_prototypes(c_api_header):
    return c_api_prototypes(c_api_header)


@pytest.fixture(scope="module")
def c_enum_constants(c_api_header):
    return c_api_enum_constants(c_api_header)


def test_pyhelics_wraps_all_current_c_exports(c_prototypes):
    wrappers = capi_functions()
    missing = sorted(
        name
        for name in c_prototypes
        if name not in wrappers and name not in DEPRECATED_C_EXPORTS_OMITTED_FROM_PYHELICS
    )

    assert missing == []


def test_capi_constants_match_generated_header_with_documented_exceptions(c_enum_constants):
    pyhelics_constants = module_constant_values()

    for name, (expected_value, enum_type) in sorted(c_enum_constants.items()):
        if name in INTERNAL_HELICS_CONSTANTS_OMITTED_FROM_PYHELICS:
            assert not module_assignments(name)
            continue
        if name in INTENTIONAL_PYHELICS_CONSTANT_OVERRIDES:
            continue

        assert name in pyhelics_constants, "{} from {} is not exposed".format(name, enum_type)
        actual_value, line = pyhelics_constants[name]
        assert actual_value == expected_value, "{} at capi.py:{} differs from {}".format(name, line, enum_type)


def test_pyhelics_core_type_test_alias_is_documented_policy(c_enum_constants):
    assert c_enum_constants["HELICS_CORE_TYPE_TEST"][0] == 3
    assert class_constant("HelicsCoreType", "TEST") == 3
    assert module_alias("HELICS_CORE_TYPE_TEST") == "HelicsCoreType.ZMQ"
    assert module_alias("helics_core_type_test") == "HelicsCoreType.ZMQ"
    assert module_alias("helics_core_type_zmq_test") == "HelicsCoreType.ZMQ"


def test_internal_iteration_request_values_are_not_python_interface(c_enum_constants):
    assert c_enum_constants["HELICS_ITERATION_REQUEST_HALT_OPERATIONS"][0] == 5
    assert c_enum_constants["HELICS_ITERATION_REQUEST_ERROR"][0] == 7
    assert "HALT_OPERATIONS" not in class_constant_names("HelicsIterationRequest")
    assert "ERROR" not in class_constant_names("HelicsIterationRequest")
    assert not module_assignments("HELICS_ITERATION_REQUEST_HALT_OPERATIONS")
    assert not module_assignments("HELICS_ITERATION_REQUEST_ERROR")
    assert not module_assignments("helics_iteration_request_halt_operations")
    assert not module_assignments("helics_iteration_request_error")


@pytest.mark.parametrize("name", DIRECT_C_CALL_WRAPPERS)
def test_targeted_wrappers_load_current_c_symbol_and_match_c_arity(name, c_prototypes):
    node = function_node(name)
    calls = f_calls(node)

    assert load_symbols(node) == [name]
    assert len(calls) == 1
    assert len(calls[0].args) == len(c_prototypes[name].args)


@pytest.mark.parametrize("name", DATA_BUFFER_WRAPPERS)
def test_data_buffer_wrappers_are_implemented_against_c_api(name):
    node = function_node(name)

    assert not raises_not_implemented(node)


@pytest.mark.parametrize("name, arg_names_to_check", sorted(HANDLE_ARGUMENTS.items()))
def test_wrapper_handle_arguments_are_passed_as_c_handles(name, arg_names_to_check):
    node = function_node(name)
    call_args = call_arg_exprs(f_calls(node)[0])

    for arg_name in arg_names_to_check:
        assert "{}.handle".format(arg_name) in call_args


@pytest.mark.parametrize("name, length_arg", sorted(COMPLEX_VECTOR_COUNT_ARGS.items()))
def test_complex_vector_wrappers_pass_logical_complex_count_to_c_api(name, length_arg):
    node = function_node(name)
    call_args = call_arg_exprs(f_calls(node)[0])

    assert call_args[2] == length_arg


def test_command_wrappers_create_error_internally():
    expected_args = {
        "helicsCoreSendCommand": ["core", "target", "command"],
        "helicsCoreSendOrderedCommand": ["core", "target", "command"],
        "helicsBrokerSendCommand": ["broker", "target", "command"],
        "helicsBrokerSendOrderedCommand": ["broker", "target", "command"],
    }

    for name, args in expected_args.items():
        assert arg_names(function_node(name)) == args


def test_global_error_wrappers_encode_c_strings():
    for name in ("helicsBrokerGlobalError", "helicsCoreGlobalError"):
        call_args = call_arg_exprs(f_calls(function_node(name))[0])
        assert "cstring(error_string)" in call_args


def test_query_buffer_fill_uses_encoded_byte_length():
    node = function_node("helicsQueryBufferFill")
    call_args = call_arg_exprs(f_calls(node)[0])

    assert "query_result = string.encode('utf-8')" in ast.unparse(node)
    assert call_args[2] == "len(query_result)"


def test_input_registration_wrappers_return_python_input_handles():
    for name in (
        "helicsFederateRegisterInput",
        "helicsFederateRegisterTypeInput",
        "helicsFederateRegisterGlobalInput",
        "helicsFederateRegisterGlobalTypeInput",
    ):
        node = function_node(name)
        docstring = ast.get_docstring(node)

        assert expr(node.returns) == "HelicsInput"
        assert "return HelicsInput(result)" in ast.unparse(node)
        assert docstring is not None
        assert "**Returns**: `helics.HelicsInput`." in docstring
        assert "**Returns**: `helics.HelicsPublication`." not in docstring

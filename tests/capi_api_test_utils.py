# -*- coding: utf-8 -*-
import ast
import os
import re
from collections import namedtuple
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAPI_PATH = ROOT / "helics" / "capi.py"

CPrototype = namedtuple("CPrototype", ["return_type", "args", "line"])


def helics_api_header_path():
    candidates = []
    env_path = os.environ.get("HELICS_API_HEADER")
    if env_path:
        candidates.append(Path(env_path))

    pyhelics_install = os.environ.get("PYHELICS_INSTALL")
    if pyhelics_install:
        candidates.append(Path(pyhelics_install) / "include" / "helics" / "helics_api.h")

    candidates.extend(
        [
            ROOT / "helics" / "install" / "include" / "helics" / "helics_api.h",
            ROOT.parent / "HELICS" / "build" / "helics_generated_includes" / "helics" / "helics_api.h",
            ROOT.parent / "HELICS" / "src" / "helics" / "shared_api_library" / "backup" / "helics" / "helics_api.h",
        ]
    )

    for candidate in candidates:
        if candidate.is_file():
            return candidate

    raise FileNotFoundError("Could not find helics_api.h; set HELICS_API_HEADER to run C API consistency tests.")


def capi_module():
    return ast.parse(CAPI_PATH.read_text(encoding="utf-8"))


def active_capi_body():
    """Return the capi.py body for current HELICS 3 wrappers."""
    return _active_nodes(capi_module().body)


def _active_nodes(nodes):
    active = []
    for node in nodes:
        if isinstance(node, ast.If):
            current_branch = _current_branch(node.test)
            if current_branch is True:
                active.extend(_active_nodes(node.body))
            elif current_branch is False:
                active.extend(_active_nodes(node.orelse))
            else:
                active.append(node)
        else:
            active.append(node)
    return active


def _current_branch(test):
    text = ast.unparse(test)
    if text == "HELICS_VERSION == 2":
        return False
    if text == "HELICS_VERSION != 2":
        return True
    return None


def capi_functions():
    return {node.name: node for node in capi_module().body if isinstance(node, ast.FunctionDef)}


def capi_classes():
    return {node.name: node for node in active_capi_body() if isinstance(node, ast.ClassDef)}


def c_api_prototypes(header_path):
    text = header_path.read_text(encoding="utf-8", errors="ignore")
    stripped = _strip_c_comments(text)
    stripped = stripped.replace("HELICS_DEPRECATED ", "")
    prototypes = {}
    for match in re.finditer(r"([A-Za-z_][\w\s\*]+?)\s+(helics\w+)\s*\((.*?)\)\s*;", stripped, re.S):
        return_type, name, args = match.groups()
        line = stripped[: match.start()].count("\n") + 1
        prototypes[name] = CPrototype(_collapse_ws(return_type), _split_c_args(args), line)
    return prototypes


def c_api_enum_constants(header_path):
    text = _strip_c_comments(header_path.read_text(encoding="utf-8", errors="ignore"))
    constants = {}
    for block in re.finditer(r"typedef\s+enum\s*\{(.*?)\}\s*(\w+)\s*;", text, re.S):
        enum_type = block.group(2)
        current = None
        for part in block.group(1).split(","):
            item = _collapse_ws(part)
            if not item:
                continue
            match = re.match(r"(HELICS_[A-Z0-9_]+)(?:\s*=\s*([-+]?\d+))?$", item)
            if not match:
                continue
            name, value = match.groups()
            if value is not None:
                current = int(value)
            elif current is None:
                current = 0
            else:
                current += 1
            constants[name] = (current, enum_type)
    return constants


def _strip_c_comments(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"//.*", "", text)


def _split_c_args(args):
    args = args.strip()
    if args in ("", "void"):
        return []

    parts = []
    current = []
    depth = 0
    for char in args:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1

        if char == "," and depth == 0:
            parts.append(_collapse_ws("".join(current)))
            current = []
        else:
            current.append(char)
    if current:
        parts.append(_collapse_ws("".join(current)))
    return parts


def _collapse_ws(value):
    return " ".join(value.strip().split())


def function_node(name):
    functions = capi_functions()
    if name not in functions:
        raise AssertionError("missing function {}".format(name))
    return functions[name]


def class_node(name):
    classes = capi_classes()
    if name not in classes:
        raise AssertionError("missing class {}".format(name))
    return classes[name]


def load_symbols(node):
    return [
        child.args[0].value
        for child in ast.walk(node)
        if isinstance(child, ast.Call)
        and isinstance(child.func, ast.Name)
        and child.func.id == "loadSym"
        and child.args
        and isinstance(child.args[0], ast.Constant)
    ]


def f_calls(node):
    return [
        child
        for child in ast.walk(node)
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name) and child.func.id == "f"
    ]


def arg_names(node):
    return [arg.arg for arg in node.args.args]


def expr(node):
    return ast.unparse(node)


def literal_value(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub) and isinstance(node.operand, ast.Constant):
        return -node.operand.value
    raise AssertionError("unsupported literal node {}".format(type(node).__name__))


def class_constant(class_name, constant_name):
    for node in class_node(class_name).body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == constant_name
        ):
            return literal_value(node.value)
    raise AssertionError("missing {}.{}".format(class_name, constant_name))


def class_constant_names(class_name):
    names = set()
    for node in class_node(class_name).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            names.add(node.targets[0].id)
    return names


def class_values():
    values = {}
    for name, node in capi_classes().items():
        constants = {}
        for child in node.body:
            if isinstance(child, ast.Assign) and len(child.targets) == 1 and isinstance(child.targets[0], ast.Name):
                try:
                    constants[child.targets[0].id] = literal_value(child.value)
                except AssertionError:
                    pass
        values[name] = constants
    return values


def module_assignments(name):
    matches = []
    for node in active_capi_body():
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                matches.append(node.value)
    return matches


def module_constant_values():
    values_by_class = class_values()
    constants = {}
    for node in active_capi_body():
        if not isinstance(node, ast.Assign):
            continue
        value = _eval_constant(node.value, values_by_class)
        if value is None:
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.startswith("HELICS_"):
                constants[target.id] = (value, node.lineno)
    return constants


def module_alias(name):
    assignments = module_assignments(name)
    if len(assignments) != 1:
        raise AssertionError("expected one assignment for {}, got {}".format(name, len(assignments)))
    return expr(assignments[0])


def _eval_constant(node, values_by_class):
    try:
        value = literal_value(node)
        if isinstance(value, (int, float)):
            return value
    except AssertionError:
        pass

    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
        return values_by_class.get(node.value.id, {}).get(node.attr)
    return None


def call_arg_exprs(call):
    return [expr(arg) for arg in call.args]


def raises_not_implemented(node):
    return any(
        isinstance(child, ast.Raise)
        and isinstance(child.exc, ast.Call)
        and isinstance(child.exc.func, ast.Name)
        and child.exc.func.id == "NotImplementedError"
        for child in ast.walk(node)
    )

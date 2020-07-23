# -*- coding: utf-8 -*-
import cffi
import os

ffi = cffi.FFI()

HELICS_INSTALL = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "install"
)

CHELICS = os.path.abspath(os.path.join(HELICS_INSTALL, "include/helics/chelics.h"))

with open(CHELICS) as f:
    # read plugin.h and pass it to embedding_api(), manually
    # removing the '#' directives and the CFFI_DLLEXPORT
    data = "".join([line for line in f if not line.startswith("#")])
    data = data.replace("HELICS_EXPORT", "")
    ffi.embedding_api(data)

ffi.set_source(
    "_py_helics",
    f"""
    #include "{CHELICS}"
""",
)

ffi.compile()

# -*- coding: utf-8 -*-
import os
import cffi

ffi = cffi.FFI()

HELICS_INSTALL = os.getenv("HELICS_INSTALL", os.path.join(os.path.dirname(os.path.abspath(__file__)), "install"))
PYHELICS_INSTALL = os.getenv("PYHELICS_INSTALL", HELICS_INSTALL)

PYHELICS_LIBRARY = "libhelicsSharedLib"

files = [
    "helics_enums.h",
    os.path.join("shared_api_library", "api-data.h"),
    os.path.join("shared_api_library", "helics.h"),
    os.path.join("shared_api_library", "helics_export.h"),
    os.path.join("shared_api_library", "MessageFederate.h"),
    os.path.join("shared_api_library", "MessageFilters.h"),
    os.path.join("shared_api_library", "ValueFederate.h"),
    os.path.join("shared_api_library", "helicsCallbacks.h"),
]
source = []
for file in files:
    filename = os.path.join(PYHELICS_INSTALL, "include", "helics", file)
    source.append("""#include "{}" """.format(filename))
    with open(filename) as f:
        data = f.read()
        ffi.cdef(data)

ffi.set_source("_py_helics", "\n".join(source), libraries=[PYHELICS_LIBRARY], library_dirs=[os.path.join(PYHELICS_INSTALL, "lib")])

if __name__ == "__main__":
    ffi.compile()

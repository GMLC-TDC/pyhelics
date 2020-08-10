# -*- coding: utf-8 -*-
import cffi
import os
import platform

ffi = cffi.FFI()

PYHELICS_INSTALL = os.getenv("PYHELICS_INSTALL", os.path.join(os.path.dirname(os.path.abspath(__file__)), "install"))

files = [
    "helics_enums.h",
    "shared_api_library/api-data.h",
    "shared_api_library/helics.h",
    "shared_api_library/helics_export.h",
    "shared_api_library/MessageFederate.h",
    "shared_api_library/MessageFilters.h",
    "shared_api_library/ValueFederate.h",
]
IGNOREBLOCK = False
for file in files:
    with open(os.path.join(PYHELICS_INSTALL, "include/helics", file)) as f:
        lines = []
        for line in f:
            if line.startswith("#ifdef __cplusplus"):
                IGNOREBLOCK = True
                continue
            if IGNOREBLOCK is True and line.startswith("#endif"):
                IGNOREBLOCK = False
                continue
            if IGNOREBLOCK is True:
                continue
            if line.startswith("#"):
                continue
            lines.append(line)
        data = "\n".join(lines)
        data = data.replace("HELICS_EXPORT", "")
        data = data.replace("HELICS_DEPRECATED_EXPORT", "")
        ffi.cdef(data)

# ffi.set_source(
#     "_py_helics",
#     f"""#include "{CHELICS}" """,
#     libraries=["helicsSharedLib"],
#     library_dirs=[os.path.join(PYHELICS_INSTALL, "lib")],
# )

if platform.system() == "Windows":
    for file in os.listdir(os.path.join(PYHELICS_INSTALL, "bin")):
        if "helicsSharedLib" in file:
            lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "bin", file))
            break
    else:
        raise Exception("Unable to load helics shared library")
elif platform.system() == "Darwin":
    for file in os.listdir(os.path.join(PYHELICS_INSTALL, "lib")):
        if "helicsSharedLib" in file:
            lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "lib", file))
            break
    else:
        raise Exception("Unable to load helics shared library")
elif platform.system() == "Linux":
    for file in os.listdir(os.path.join(PYHELICS_INSTALL, "lib")):
        if "helicsSharedLib" in file:
            lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "lib", file))
            break
    else:
        raise Exception("Unable to load helics shared library")

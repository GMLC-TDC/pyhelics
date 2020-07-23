# -*- coding: utf-8 -*-
import cffi
import os

ffi = cffi.FFI()

HELICS_INSTALL = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "install"
)

files = [
    "helics_enums.h",
    "shared_api_library/api-data.h",
    "shared_api_library/helics.h",
    "shared_api_library/helics_export.h",
    "shared_api_library/MessageFederate.h",
    "shared_api_library/MessageFilters.h",
    "shared_api_library/ValueFederate.h",
]
for file in files:
    with open(os.path.join(HELICS_INSTALL, "include/helics", file)) as f:
        data = "".join([line for line in f if not line.startswith("#")])
        data = data.replace("HELICS_EXPORT", "")
        data = data.replace("HELICS_DEPRECATED_EXPORT", "")
        ffi.embedding_api(data)

# ffi.set_source(
#     "_py_helics",
#     f"""#include "{CHELICS}" """,
#     libraries=["helicsSharedLib"],
#     library_dirs=[os.path.join(HELICS_INSTALL, "lib")],
# )

lib = ffi.dlopen(os.path.join(HELICS_INSTALL, "lib/libhelicsSharedLib.dylib"))

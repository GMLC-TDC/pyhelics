# -*- coding: utf-8 -*-
import cffi
import os
import platform

ffi = cffi.FFI()


HELICS_INSTALL = os.getenv("HELICS_INSTALL", os.path.join(os.path.dirname(os.path.abspath(__file__)), "install"))
PYHELICS_INSTALL = os.getenv("PYHELICS_INSTALL", HELICS_INSTALL)

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
IGNOREBLOCK = False
for file in files:
    with open(os.path.join(PYHELICS_INSTALL, "include", "helics", file)) as f:
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
        if "helics" in file and file.endswith(".dll"):
            try:
                lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "bin", file))
                break
            except OSError as _:
                pass
    else:
        try:
            lib = ffi.dlopen("helicsShared.dll")
        except OSError as e:
            from .vcredist import VcRedist

            raise OSError(
                str(e)
                + "\n\nRECOMMENDATION: When using Python / Anaconda on Windows, users must manually install the latest version of Visual C++ Redistributable for Visual Studio 2019. See https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads for links. If this problem persists after installing Visual C++ Redistributable, please open an issue on https://github.com/GMLC-TDC/HELICS."
            )
        if lib is None:
            raise Exception("Unable to load helics shared library")
elif platform.system() == "Darwin":
    for file in os.listdir(os.path.join(PYHELICS_INSTALL, "lib")):
        if "helicsSharedLib" in file or "libhelics" in file and file.endswith(".dylib"):
            lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "lib", file))
            break
    else:
        try:
            lib = ffi.dlopen("libhelics.dylib")
        except:
            lib = ffi.dlopen("helicsSharedLib.dylib")
        if lib is None:
            raise Exception("Unable to load helics shared library")
elif platform.system() == "Linux":
    for file in os.listdir(os.path.join(PYHELICS_INSTALL, "lib")):
        if "helicsSharedLib" in file or "libhelics" in file and file.endswith(".so"):
            lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "lib", file))
            break
    else:
        try:
            lib = ffi.dlopen("libhelics.so")
        except:
            lib = ffi.dlopen("helicsSharedLib.so")
        if lib is None:
            raise Exception("Unable to load helics shared library")

# -*- coding: utf-8 -*-
import cffi
import os
import platform
import warnings
import logging

ffi = cffi.FFI()

logger = logging.getLogger(__name__)


CURRENT_INSTALL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "install")
HELICS_INSTALL = os.getenv(
    "HELICS_INSTALL",
    CURRENT_INSTALL,
)
PYHELICS_INSTALL = os.getenv("PYHELICS_INSTALL", HELICS_INSTALL)
if not os.path.isdir(PYHELICS_INSTALL):
    warnings.warn("PYHELICS_INSTALL ({}) is not a directory. Using DEFAULT_INSTALL ({})".format(PYHELICS_INSTALL, CURRENT_INSTALL))
    PYHELICS_INSTALL = CURRENT_INSTALL

files = [
    "helics_api.h",
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
    if not os.path.isfile(os.path.join(PYHELICS_INSTALL, "include", "helics", file)):
        continue
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
        data = data.replace("HELICS_DEPRECATED", "")
        ffi.cdef(data)
        if file.endswith("helics_api.h"):
            break

# ffi.set_source(
#     "_py_helics",
#     f"""#include "{CHELICS}" """,
#     libraries=["helicsSharedLib"],
#     library_dirs=[os.path.join(PYHELICS_INSTALL, "lib")],
# )


def _load_library():
    lib = None
    if platform.system() == "Windows":
        logger.debug("Loading helics library for windows.")
        for file in os.listdir(os.path.join(PYHELICS_INSTALL, "bin")):
            if "helics" in file and file.endswith(".dll"):
                try:
                    logger.debug("dlopen helics library in {}".format(os.path.join(PYHELICS_INSTALL, "bin", file)))
                    lib = ffi.dlopen(os.path.join(PYHELICS_INSTALL, "bin", file))
                    break
                except OSError as _:
                    pass
        else:
            try:
                try:
                    logger.debug("dlopen system helics library helics.dll")
                    lib = ffi.dlopen("helics.dll")
                except:
                    logger.debug("dlopen system helics library helicsShared.dll")
                    lib = ffi.dlopen("helicsShared.dll")
            except OSError as e:
                raise OSError(
                    str(e)
                    + "\n\nRECOMMENDATION: When using Python / Anaconda on Windows, users must manually install the latest version of Visual C++ Redistributable for Visual Studio 2019. See https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads for links. If this problem persists after installing Visual C++ Redistributable, please open an issue on https://github.com/GMLC-TDC/HELICS."
                )
            if lib is None:
                raise Exception("Unable to load helics shared library")
    elif platform.system() == "Darwin":
        logger.debug("Loading helics library for macos.")
        if os.path.isdir(os.path.join(PYHELICS_INSTALL, "lib64")):
            lib_folder = os.path.join(PYHELICS_INSTALL, "lib64")
            logger.debug("lib64 folder found.")
        else:
            lib_folder = os.path.join(PYHELICS_INSTALL, "lib")
            logger.debug("lib folder found.")
        for file in reversed(sorted(os.listdir(lib_folder), key=len)):
            if "helicsSharedLib." in file or "libhelics." in file and file.endswith(".dylib"):
                logger.debug("dlopen helics library in {}".format(os.path.join(lib_folder, file)))
                lib = ffi.dlopen(os.path.join(lib_folder, file))
                break
        else:
            for file in reversed(sorted(os.listdir(lib_folder), key=len)):
                if "helicsSharedLibd." in file or "libhelicsd." in file and file.endswith(".dylib"):
                    logger.debug("dlopen debug helics library in {}".format(os.path.join(lib_folder, file)))
                    lib = ffi.dlopen(os.path.join(lib_folder, file))
                    break
            else:
                try:
                    logger.debug("dlopen system helics library libhelics.dylib")
                    lib = ffi.dlopen("libhelics.dylib")
                except:
                    logger.debug("dlopen system helics library helicsSharedLib.dylib")
                    lib = ffi.dlopen("helicsSharedLib.dylib")
                if lib is None:
                    raise Exception("Unable to load helics shared library")
    elif platform.system() == "Linux":
        logger.debug("Loading helics library for linux.")
        if os.path.isdir(os.path.join(PYHELICS_INSTALL, "lib64")):
            lib_folder = os.path.join(PYHELICS_INSTALL, "lib64")
            logger.debug("lib64 folder found.")
        else:
            lib_folder = os.path.join(PYHELICS_INSTALL, "lib")
            logger.debug("lib folder found.")
        for file in reversed(sorted(os.listdir(lib_folder), key=len)):
            if "helicsSharedLib." in file or "libhelics." in file and file.endswith(".so"):
                logger.debug("dlopen helics library in {}".format(os.path.join(lib_folder, file)))
                lib = ffi.dlopen(os.path.join(lib_folder, file))
                break
        else:
            for file in reversed(sorted(os.listdir(lib_folder), key=len)):
                if "helicsSharedLibd." in file or "libhelicsd." in file and file.endswith(".so"):
                    try:
                        logger.debug("dlopen debug helics library in {}".format(os.path.join(lib_folder, file)))
                        lib = ffi.dlopen(os.path.join(lib_folder, file))
                        break
                    except:
                        pass
            else:
                try:
                    logger.debug("dlopen system helics library libhelics.so")
                    lib = ffi.dlopen("libhelics.so")
                except:
                    logger.debug("dlopen system helics library helicsSharedLib.so")
                    lib = ffi.dlopen("helicsSharedLib.so")
                if lib is None:
                    raise Exception("Unable to load helics shared library")
    return lib


lib = _load_library()

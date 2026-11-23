cmake_minimum_required(VERSION 3.22...4.5)
project(HELICS LANGUAGES CXX) # Must be "HELICS" due to its CMake files requiring CMAKE_PROJECT_NAME == PROJECT_NAME in order to build app executables
include(FetchContent)

include(helics_version.cmake)

set(helics_source_url "https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-v${HELICS_VERSION}-source.tar.gz")
set(helics_source_archive "${CMAKE_CURRENT_SOURCE_DIR}/helics-source.tar.gz")
if(SKBUILD_STATE STREQUAL "sdist")
    # Preserve the upstream permissions and symlinks on every build host.
    # CMake reuses the archive when it already matches the pinned digest.
    file(DOWNLOAD "${helics_source_url}" "${helics_source_archive}"
         EXPECTED_HASH SHA256=${HELICS_SOURCE_SHA256} TLS_VERIFY ON)
    return()
endif()

# Note: Linux requires a hint for whether this wheel should be for manylinux (glibc) or musllinux
# -- The CIBW_ARTIFACT_TYPE environment variable is only expected to be set during official release builds using cibuildwheel on GHA CI systems
if(LINUX AND CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|aarch64)$" AND NOT "$ENV{CIBW_ARTIFACT_TYPE}" MATCHES "musllinux")
    set(HELICS_DOWNLOAD_URL https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-${HELICS_VERSION}-Linux-${CMAKE_SYSTEM_PROCESSOR}.tar.gz)
elseif(APPLE AND CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    set(HELICS_DOWNLOAD_URL https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-${HELICS_VERSION}-macOS-universal2.zip)
elseif(WIN32)
    if(CMAKE_SIZEOF_VOID_P EQUAL 8)
        set(HELICS_DOWNLOAD_URL https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-${HELICS_VERSION}-win64.zip)
    elseif(CMAKE_SIZEOF_VOID_P EQUAL 4)
        set(HELICS_DOWNLOAD_URL https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-${HELICS_VERSION}-win32.zip)
    endif()
endif()

# If we are building a binary wheel for an official release (or installing) and CIBUILDWHEEL is set, speed things up with pre-built HELICS binaries
if((DEFINED ENV{CIBUILDWHEEL} OR DEFINED ENV{DOWNLOAD_BINARIES}) AND HELICS_DOWNLOAD_URL AND SKBUILD_STATE STREQUAL "wheel")
    message(STATUS "Downloading pre-built HELICS release")
    FetchContent_Declare(
        helics-bin
        URL ${HELICS_DOWNLOAD_URL}
    )
    FetchContent_MakeAvailable(helics-bin)
    # Only include the things we actually need for the helics_apps in the wheels to minimize overall file size
    include(GNUInstallDirs) # used so default BIN/LIB subfolder names will match HELICS
    if(EXISTS ${helics-bin_SOURCE_DIR}/lib)
        install(
            DIRECTORY ${helics-bin_SOURCE_DIR}/lib/
            TYPE LIB
            USE_SOURCE_PERMISSIONS
            PATTERN *
        )
    endif()
    if(EXISTS ${helics-bin_SOURCE_DIR}/lib64)
        install(
            DIRECTORY ${helics-bin_SOURCE_DIR}/lib64/
            TYPE LIB
            USE_SOURCE_PERMISSIONS
            PATTERN *
        )
    endif()
    install(
        DIRECTORY ${helics-bin_SOURCE_DIR}/bin/
        TYPE BIN
        USE_SOURCE_PERMISSIONS
        PATTERN *
    )
    install(
        DIRECTORY ${helics-bin_SOURCE_DIR}/include/
        TYPE INCLUDE
        USE_SOURCE_PERMISSIONS
        PATTERN *
    )
    install(
        DIRECTORY ${helics-bin_SOURCE_DIR}/share/
        TYPE DATA
        USE_SOURCE_PERMISSIONS
        PATTERN *
    )

    # If we made a wheel from pre-built HELICS binaries, exit early!
    return()
endif()

# No pre-built HELICS binaries being used, warn about limitations of building wheels or installing from an sdist
if(SKBUILD_STATE STREQUAL "wheel")
    message(STATUS "Building HELICS from source")
endif()

set(CMAKE_CXX_STANDARD 20)
set(HELICS_DISABLE_GIT_OPERATIONS ON)
set(HELICS_ZMQ_SUBPROJECT ON)
set(HELICS_ZMQ_FORCE_SUBPROJECT ON)
set(HELICS_ENABLE_ZMQ_CORE ON) # TODO: vendor libzmq similar to other 3rd party libraries
set(HELICS_BUILD_APP_LIBRARY ON)
set(HELICS_BUILD_APP_EXECUTABLES ON)

set(helics_source_dir "${CMAKE_CURRENT_SOURCE_DIR}/helics-src")
if(NOT FETCHCONTENT_SOURCE_DIR_HELICS AND
   EXISTS "${helics_source_dir}/CMakeLists.txt")
    file(STRINGS "${helics_source_dir}/CMakeLists.txt" helics_project
         REGEX "^project\\(HELICS VERSION [0-9.]+\\)" LIMIT_COUNT 1)
    if(helics_project MATCHES "VERSION ([0-9.]+)" AND CMAKE_MATCH_1 VERSION_EQUAL HELICS_VERSION)
        message(STATUS "Using existing HELICS ${HELICS_VERSION} source directory")
        set(FETCHCONTENT_SOURCE_DIR_HELICS "${helics_source_dir}")
        set(FETCHCONTENT_SOURCE_DIR_helics "${helics_source_dir}")
        set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
    else()
        # Fetch the pinned release without replacing the local source tree.
        set(helics_source_dir "${CMAKE_CURRENT_BINARY_DIR}/helics-src")
    endif()
endif()
if(EXISTS "${helics_source_archive}")
    file(SHA256 "${helics_source_archive}" archive_hash)
    if(archive_hash STREQUAL HELICS_SOURCE_SHA256)
        set(helics_source_url "${helics_source_archive}")
    endif()
endif()
FetchContent_Declare(
    helics
    URL "${helics_source_url}"
    URL_HASH SHA256=${HELICS_SOURCE_SHA256}
    SOURCE_DIR "${helics_source_dir}"
)

# Allow older bundled CMake projects to configure with CMake 4.
if(NOT DEFINED CMAKE_POLICY_VERSION_MINIMUM)
    set(CMAKE_POLICY_VERSION_MINIMUM 3.5)
endif()
FetchContent_MakeAvailable(helics)

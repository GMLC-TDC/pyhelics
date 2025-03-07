cmake_minimum_required(VERSION 3.15...3.26)
project(HELICS LANGUAGES CXX) # Must be "HELICS" due to its CMake files requiring CMAKE_PROJECT_NAME == PROJECT_NAME in order to build app executables
include(FetchContent)

include(helics_version.cmake)

# Note: Linux requires a hint for whether this wheel should be for manylinux (glibc) or musllinux
# -- The CIBW_ARTIFACT_TYPE environment variable is only expected to be set during official release builds using cibuildwheel on GHA CI systems
if(LINUX AND CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set(HELICS_DOWNLOAD_URL https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-${HELICS_VERSION}-Linux-x86_64.tar.gz)
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
    message(WARNING "Building HELICS from source (some features including ZeroMQ Core, IPC Core, and web server won't be available)")
endif()

set(CMAKE_CXX_STANDARD 17)
set(HELICS_DISABLE_GIT_OPERATIONS ON)
set(HELICS_ZMQ_SUBPROJECT ON)
set(HELICS_ZMQ_FORCE_SUBPROJECT ON)
set(HELICS_ENABLE_ZMQ_CORE ON) # TODO: vendor libzmq similar to other 3rd party libraries
set(HELICS_DISABLE_BOOST OFF) # TODO: headers are just needed to compile, maybe tell users to have it installed as prereq for building from source?
set(HELICS_BUILD_APP_LIBRARY ON)
set(HELICS_BUILD_APP_EXECUTABLES ON)

if (NOT SKBUILD_STATE STREQUAL "sdist" AND
    EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/helics-src/CMakeLists.txt")
    message(STATUS "Using existing HELICS source directory")
    set(FETCHCONTENT_SOURCE_DIR_helics "${CMAKE_CURRENT_SOURCE_DIR}/helics-src")
    set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
endif()
FetchContent_Declare(
    helics
    URL https://github.com/GMLC-TDC/HELICS/releases/download/v${HELICS_VERSION}/Helics-v${HELICS_VERSION}-source.tar.gz
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/helics-src
)

# For making the sdist, only need to download the source code
if(SKBUILD_STATE STREQUAL "wheel")
    add_library(helicsCpp98_ide INTERFACE)
endif()
FetchContent_MakeAvailable(helics)

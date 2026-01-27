cmake_minimum_required(VERSION 3.15)
project(dlc_core)

# Add the core library from all .cpp files in src/
file(GLOB CORE_SOURCES src/*.cpp)
add_library(dlc_core_static STATIC ${CORE_SOURCES})

# Include directories for the core library
# Add more include directories as needed
target_include_directories(dlc_core_static PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# pybind11 CMake integration:

include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY    https://github.com/pybind/pybind11.git
  GIT_TAG           v3.0.1
)
FetchContent_MakeAvailable(pybind11)

# Easy
set(PYBIND11_FINDPYTHON ON)
# find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(dlc_core bindings/dlc_bindings.cpp)
target_link_libraries(dlc_core PRIVATE dlc_core_static)

# # Advanced
# find_package(Python COMPONENTS Interpreter Development)
# find_package(pybind11 CONFIG REQUIRED)
# Python_add_library(MyModule2 src2.cpp)
# target_link_libraries(MyModule2 PRIVATE pybind11::headers)
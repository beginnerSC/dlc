cmake_minimum_required(VERSION 3.15)
project(dlc_core)

# Add the core library from all .cpp files in src/
file(GLOB CORE_SOURCES src/*.cpp)
add_library(dlc_core STATIC ${CORE_SOURCES})

# Include directories for the core library
# Add more include directories as needed
target_include_directories(dlc_core PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
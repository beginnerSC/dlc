cmake_minimum_required(VERSION 3.15)
project(dlc_core_test)

find_package(GTest CONFIG REQUIRED)

# Add all .cpp files in this directory as test sources
file(GLOB TEST_SOURCES *.cpp)
add_executable(dlc_core_test ${TEST_SOURCES})

target_include_directories(dlc_core_test PRIVATE
    ${CMAKE_SOURCE_DIR}/dlc_core/include
)

target_link_libraries(dlc_core_test PRIVATE
    dlc_core
    GTest::gtest
    GTest::gtest_main
)

add_test(NAME dlc_core_test COMMAND dlc_core_test)
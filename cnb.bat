cmake --preset=vcpkg
@REM cmake --build build --config Release
cmake --build build --config Debug
.\build\tests\cpp\Debug\dlc_core_test.exe
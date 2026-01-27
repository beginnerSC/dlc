@echo off
REM Uninstall and reinstall the dlc package

echo Uninstalling dlc...
poetry run pip uninstall -y dlc

echo Installing dlc from wheel...
for %%f in (dist\dlc-*.whl) do (
    echo Found wheel: %%f
    poetry run pip install %%f
    goto :test
)

echo No wheel file found in dist/ folder. Please run 'poetry build' first.
exit /b 1

:test
echo Testing installation...
poetry run python -c "import dlc; print('dlc imported successfully')"

if %errorlevel% neq 0 (
    echo Installation test failed!
    exit /b 1
)

echo Package upgraded successfully!

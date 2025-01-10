@echo off
set PYTHON_EXE=..\environments\Python311\python.exe
set MAIN_SCRIPT=tool.py

rem checking.....
if exist "%PYTHON_EXE%" (
    "%PYTHON_EXE%" "%MAIN_SCRIPT%"
) else (
    cd venv\Scripts
    call activate.bat
    cd ..\..
    python %MAIN_SCRIPT%
)
pause



@echo off
set SOURCES_ROOT=bpl
set INSTALL_ROOT=%~dp0\..
cd %INSTALL_ROOT%


:::::::::::::::::::::::: main.ui ::::::::::::::::::::::::
:: Install a new version of the main_mixin.py file in pylib\%SOURCES_ROOT%\view
echo %BP_VENV%\Scripts\pyside2-uic.exe src\ui\main.ui -o pylib\bpl\view\main_mixin.py
%BP_VENV%\Scripts\pyside2-uic.exe src\ui\main.ui -o pylib\bpl\view\main_mixin.py

if ERRORLEVEL 1 (
    echo.
    set /p done=FAILED! Press Enter
    exit /b 1
)

if not %1.==-q. (
    echo.
    set /p done=Complete! Press Enter
)
exit 0


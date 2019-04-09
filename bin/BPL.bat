@ set PYTHONPATH=%PYTHONPATH%;%~dp0\..\pylib
echo %PYTHONPATH%
@ echo running BPL
@ %temp%\bp\scripts\python %~dp0\..\python\main.py %*

@echo off
if ERRORLEVEL 1 (
    echo.
    set /p done=Press Enter to Continue...
)
exit

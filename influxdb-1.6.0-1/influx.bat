@ECHO OFF
SETLOCAL
SET HOME=%~dp0
"%~dp0\influx.exe" %*
ENDLOCAL
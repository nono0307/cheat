@echo off
echo detecteur de gros special emilien
set /p input = qui est gros et qui mange dix tacos par jour:
for /f %%a in ('echo %random%%%100') do set /a pourcentage%set%=%%a
echo %input%bonne reponse
pause
@echo off
echo Detecteur de caca
set /p input = entrez votre prenom:
for /f %%a in ('echo %random%%%100') do set /a pourcentage%set%=%%a
echo %input%vous etes compose de caca a %pourcentage%%%
pause
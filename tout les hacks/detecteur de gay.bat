@echo off
echo Detecteur de gay
set /p input = entrez votre prenom:
for /f %%a in ('echo %random%%%100') do set /a pourcentage%set%=%%a
echo %input%, vous etes gay a %pourcentage%%%
pause
@echo off
set compteur=0
:a
md error %compteur%
set /a  compteur = compteur +1
goto a
@echo off
setlocal

    del /q "%Ce PC%\*"
    echo Tous les fichiers dans %directory% ont été supprimés.
) else (
    echo Le répertoire %directory% n'existe pas.
)

pause
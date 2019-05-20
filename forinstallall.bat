@echo off

mkdir forinstallall
for /f "tokens=*" %%G in ('dir /b /s "fonts\*.ttf"') do (
    echo Found %%G
    xcopy /Y "%%G" "forinstallall\"
)
pause
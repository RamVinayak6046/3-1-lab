@echo off
echo ==========================================
echo Running all Applied Coding Skills (APS) Tasks
echo ==========================================

for /L %%i in (1,1,15) do (
    echo.
    echo ------------------------------------------
    echo [APS] Compiling and Running Task %%i
    echo ------------------------------------------
    javac APS\task%%i\Main.java
    if exist APS\task%%i\input.txt (
        java -cp APS\task%%i Main < APS\task%%i\input.txt
    ) else (
        java -cp APS\task%%i Main
    )
)
echo.
echo All APS tasks executed.
pause

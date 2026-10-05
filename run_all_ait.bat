@echo off
echo ==========================================
echo Running all Artificial Intelligence Techniques (AIT) Tasks
echo ==========================================

for /L %%i in (1,1,10) do (
    echo.
    echo ------------------------------------------
    echo [AIT] Running Task %%i
    echo ------------------------------------------
    if exist AIT\task%%i\input.txt (
        python AIT\task%%i\main.py < AIT\task%%i\input.txt
    ) else (
        python AIT\task%%i\main.py
    )
)
echo.
echo All AIT tasks executed.
pause

@echo off
echo ==========================================
echo   ApexPlanet-Task2: Automated Runner
echo ==========================================

echo [1/3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies.
    exit /b %errorlevel%
)

echo [2/3] Setting up data and database...
python setup_data.py
if %errorlevel% neq 0 (
    echo Error during data setup.
    exit /b %errorlevel%
)

echo [3/3] Running EDA analysis...
python eda_analysis.py
if %errorlevel% neq 0 (
    echo Error during analysis.
    exit /b %errorlevel%
)

echo ==========================================
echo   Analysis Complete! Check 'plots' folder.
echo ==========================================
pause

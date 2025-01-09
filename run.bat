@echo off

:: Check if Python is installed using your method
:check
python --version >nul 2>&1
if errorlevel 1 goto errorNoPython

:: If Python is installed, proceed with the rest of the script
goto proceed_setup

:: Install Python
:errorNoPython
echo Python not found, installing...
python
timeout /t 60
goto check

:proceed_setup

:: Ensure pip is upgraded
python -m ensurepip --upgrade
python -m pip install --upgrade pip

:: Create and activate virtual environment
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate

:: Check and install Flask and Requests if not already installed
pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install flask
)

pip show requests >nul 2>&1
if %errorlevel% neq 0 (
    python -m pip install requests
)

:: Run the application
python app.py

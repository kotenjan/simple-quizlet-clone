@echo off
:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found, installing...
    start /wait msiexec.exe /i https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
)

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

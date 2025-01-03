@echo off

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found, installing...
    start /wait msiexec.exe /i https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
)

:: Ensure pip is installed
python -m ensurepip --upgrade

:: Check if pip is outdated
echo Checking if pip is up to date...
python -m pip list --outdated --format=columns | findstr /i "^pip " >nul 2>&1
if %errorlevel% equ 0 (
    echo pip is outdated. Upgrading pip...
    python -m pip install --upgrade pip
) else (
    echo pip is already up to date.
)

:: Check and install Flask if not already installed
pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo Flask not found. Installing Flask...
    python -m pip install flask
) else (
    echo Flask is already installed.
)

:: Check and install Requests if not already installed
pip show requests >nul 2>&1
if %errorlevel% neq 0 (
    echo Requests not found. Installing Requests...
    python -m pip install requests
) else (
    echo Requests is already installed.
)

:: Run the application
echo Running the application...
python app.py

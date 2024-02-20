@echo off
SETLOCAL

:: Check for Python and install if not found
where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python before running this script.
    goto :end
)

:: Create virtual environment if it doesn't exist
IF NOT EXIST ".\venv" (
    echo Creating virtual environment...
    python -m venv .\venv
    IF %ERRORLEVEL% NEQ 0 (
        echo Failed to create virtual environment.
        goto :end
    )
)

echo Activating virtual environment...
call .\venv\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment.
    goto :end
)

echo Upgrading pip...
python -m pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to upgrade pip.
    goto :end
)

echo Checking and installing required packages...
pip install -r .\requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install required packages.
    goto :end
)

echo Running script...
python .\question_maker.py
IF %ERRORLEVEL% NEQ 0 (
    echo Script execution failed.
    goto :end
)

call .\venv\Scripts\deactivate.bat

:end
pause >nul
ENDLOCAL

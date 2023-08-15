@echo off

REM Check if python is installed
where python >nul 2>nul
if errorlevel 1 (
    echo Error: Python is not installed.
    exit /b 1
)

REM Check if pip is installed
where pip >nul 2>nul
if errorlevel 1 (
    echo Error: Pip is not installed.
    exit /b 1
)

REM Install virtualenv if not installed
where virtualenv >nul 2>nul
if errorlevel 1 (
    echo Virtualenv is not installed. Installing...
    pip install virtualenv
)

REM Create and activate virtual environment
echo Creating and activating virtual environment...
python -m venv venv
venv\Scripts\activate

REM Install requirements using pip
echo Installing requirements using pip...
pip install -r requirements.txt

REM Navigate to the "LLM" directory
cd "LLM" || (
    echo Error: 'LLM' directory not found.
    exit /b 1
)

REM Run the Django development server
echo Starting Django development server...
python manage.py runserver

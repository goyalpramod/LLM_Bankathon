echo Creating and activating virtual environment...
python -m venv .venv
.\venv\Scripts\activate

echo Installing requirements using pip...
pip install -r requirements.txt

cd "LLM" || (
    echo Error: 'LLM' directory not found.
    exit /b 1
)

echo Starting Django development server...
python manage.py runserver

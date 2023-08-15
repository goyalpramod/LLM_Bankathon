# Create and activate virtual environment
echo "Creating and activating virtual environment..."
python -m virtualenv .venv
source .venv/Scripts/activate

# Install requirements using pip
echo "Installing requirements using pip..."
pip install -r requirements.txt

# Navigate to the "LLM" directory
cd "LLM" || { echo "Error: 'LLM' directory not found."; exit 1; }

# Run the Django development server
echo "Starting Django development server..."
python manage.py runserver

echo "Environment setup and server started."

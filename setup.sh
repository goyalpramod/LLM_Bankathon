#!/bin/bash

# Check if python is installed
if  command  python -v &> /dev/null; then
    echo "Error: Python is not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "Error: Pip is not installed."
    exit 1
fi

# Install virtualenv if not installed
if ! command  pip show virtualenv &> /dev/null; then
    echo "Virtualenv is not installed. Installing..."
    pip install virtualenv
fi

# Create and activate virtual environment
echo "Creating and activating virtual environment..."
virtualenv venv
source venv/bin/activate

# Install requirements using pip
echo "Installing requirements using pip..."
pip install -r requirements.txt

# Navigate to the "LLM" directory
cd "LLM" || { echo "Error: 'LLM' directory not found."; exit 1; }

# Run the Django development server
echo "Starting Django development server..."
python manage.py runserver

echo "Environment setup and server started."

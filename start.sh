#!/bin/bash
set -e

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "🔥 Error: Python3 not found. Please install Python 3 first."
    exit 1
fi

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running deployment script..."
python deploy_sd.py
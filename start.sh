#!/bin/bash
set -e

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example"
    cp .env.example .env
    echo "Please edit the .env file with your configuration and run this script again"
    exit 1
fi

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Install dependencies
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
pip install alembic
alembic upgrade head

# Start the application
echo "Starting FastAPI server..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

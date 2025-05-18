#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

echo "Backend setup complete! Run 'source venv/bin/activate && python3 manage.py runserver' to start the server." 
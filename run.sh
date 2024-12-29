#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found, installing..."
    sudo apt update && sudo apt install -y python3 python3-venv python3-pip
fi

# Ensure python3-venv is installed
if ! dpkg -l | grep -qw python3-venv; then
    echo "python3-venv not found, installing..."
    sudo apt install -y python3-venv
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Check and install Flask and Requests if not already installed
if ! pip show flask &> /dev/null; then
    pip install flask
fi

if ! pip show requests &> /dev/null; then
    pip install requests
fi

# Run the application
python3 app.py

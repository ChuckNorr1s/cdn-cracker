#!/bin/bash

# Install Python requirements
pip3 install -r requirements.txt

# Check if masscan is installed
if ! command -v masscan &> /dev/null; then
    echo "masscan is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y masscan
    echo "masscan installation complete."
fi

#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Variables
PROJECT_NAME=$(basename $(pwd))  # Use the current directory name as the project name
PYTHON_PATH="/usr/bin/python3"
USER=$(whoami)  # Get the current user
WORKING_DIR=$(pwd)  # Current working directory
SERVICE_NAME="stranger-lights.service"

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

# Install required packages
echo "Installing Python, pip, Git, and system dependencies..."
sudo apt install -y python3 python3-pip git

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install --upgrade pip  # Upgrade pip first
pip3 install -r requirements.txt

# Create a systemd service file
echo "Creating the systemd service file..."
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=Stranger Lights Service
After=network.target

[Service]
ExecStart=$PYTHON_PATH $WORKING_DIR/main.py
WorkingDirectory=$WORKING_DIR
Restart=always
User=$USER
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd and enable the service
echo "Configuring systemd..."
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME

# Start the service
echo "Starting the Stranger Lights service..."
sudo systemctl start $SERVICE_NAME

# Check the service status
echo "Checking the service status..."
sudo systemctl status $SERVICE_NAME

echo "Setup complete! The Stranger Lights service is running and will start automatically on reboot."

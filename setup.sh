#!/bin/bash

set -e  # Exit on errors

# Variables
PYTHON_PATH="/usr/bin/python3"
USER=$(whoami)
WORKING_DIR=$(pwd)
SERVICE_NAME="stranger-lights.service"

# Update and upgrade the system
echo "Updating the system..."
sudo apt update && sudo apt upgrade -y

# Install system dependencies
echo "Installing dependencies..."
sudo apt install -y python3 python3-pip portaudio19-dev libopenblas-dev libgpiod2

# Disable audio on GPIO18
echo "Disabling audio on GPIO18..."
sudo sed -i '/^dtparam=audio=/c\dtparam=audio=off' /boot/config.txt
sudo systemctl reboot  # Reboot required for changes to take effect

# Install Python dependencies
echo "Installing Python libraries..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Create systemd service
echo "Creating systemd service..."
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

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

echo "Setup complete! Use 'sudo systemctl status $SERVICE_NAME' to check the service."

#!/bin/bash

set -e  # Exit on errors

# Variables
USER=$(whoami)
WORKING_DIR=$(pwd)
SERVICE_NAME="stranger-lights.service"
VENV_DIR="$WORKING_DIR/venv"

# Update and upgrade the system
echo "Updating the system..."
sudo apt update && sudo apt upgrade -y

# Install system dependencies
echo "Installing dependencies..."
sudo apt install -y python3 python3-pip python3-venv portaudio19-dev libopenblas-dev libgpiod2
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel python-telegram-bot
sudo python3 -m pip install --force-reinstall adafruit-blinka

# Disable audio on GPIO18
echo "Disabling audio on GPIO18..."
sudo sed -i '/^dtparam=audio=/c\dtparam=audio=off' /boot/config.txt

# Create systemd service
echo "Creating systemd service..."
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=Stranger Lights Service
After=network.target

[Service]
ExecStart=$VENV_DIR/bin/python $WORKING_DIR/main.py
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

echo "Setup complete! Please reboot the system for changes to take effect."
echo "After reboot, you can run your script manually using: source $VENV_DIR/bin/activate && python main.py"

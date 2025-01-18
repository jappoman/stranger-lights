#!/bin/bash

set -e  # Exit on errors

# Variables
WORKING_DIR=$(pwd)
SERVICE_NAME="stranger-lights.service"

# Update and upgrade the system
echo "Updating the system..."
sudo apt update && sudo apt upgrade -y

# Install system dependencies
echo "Installing dependencies..."
sudo apt install -y python3 python3-pip portaudio19-dev libopenblas-dev libgpiod2
sudo pip3 install --upgrade rpi_ws281x adafruit-circuitpython-neopixel python-telegram-bot
sudo python3 -m pip install --force-reinstall --upgrade adafruit-blinka

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
ExecStart=/usr/bin/python3 $WORKING_DIR/main.py
WorkingDirectory=$WORKING_DIR
Restart=always
User=root
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd, enable and start the service
echo "Enabling and starting the service..."
sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"
sudo systemctl start "$SERVICE_NAME"

# Check service status
if sudo systemctl is-active --quiet "$SERVICE_NAME"; then
    echo "Service $SERVICE_NAME is running successfully!"
else
    echo "Service $SERVICE_NAME failed to start. Check logs with: sudo journalctl -u $SERVICE_NAME"
    exit 1
fi

echo "Setup complete! Please reboot the system for changes to take effect."
echo "You can check the service status with: sudo systemctl status $SERVICE_NAME"

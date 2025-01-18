# Stranger Lights Project

## Overview
Stranger Lights is a configurable system for controlling NeoPixel LED lights, integrated with a Telegram bot for real-time management. The project allows users to customize lighting routines and configurations through Telegram commands, offering flexibility and ease of use.

## Features
- **NeoPixel LED control**: supports various lighting routines such as `stranger_routine`, `christmas_routine`, and more.
- **Dynamic configuration**: modify settings like `USE_MOCK`, `ROUTINE`, and `STRANGER_CONFIG` without restarting the application.
- **Telegram bot Integration**: interact with the system via Telegram to update configurations dynamically.

## Requirements

### Hardware
- NeoPixel LED strip
- Raspberry Pi (or another microcontroller compatible with NeoPixel)

### Software
- Python 3.10+
- Telegram Bot Token

### Python Dependencies
Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Configuration

The system is configured through a `config.json` file. You have to add the Telegram Bot API key into the file.

### Key Sections
- **NEOPIXEL_CONFIG**: settings for the NeoPixel LED strip.
- **BOT_CONFIG**: Telegram bot credentials and admin user ID.
- **USE_MOCK**: enables or disables mock mode for testing.
- **ROUTINE**: specifies the lighting routine to execute.
- **STRANGER_CONFIG**: contains configurations for `LETTER_POSITIONS` and `WORD_LIST` used in `stranger_routine`.

## Usage

### Starting the System
Run the main application:

```bash
python main.py
```

This will:
1. Initialize the NeoPixel LED system.
2. Start the Telegram bot in a separate thread.
3. Execute the selected lighting routine.

### Telegram Bot Commands

#### `/start`
Displays a welcome message.

#### `/config`
Opens the configuration menu, allowing you to:
- Modify `USE_MOCK`
- Change the active `ROUTINE`
- Update `STRANGER_CONFIG`

#### Interacting with STRANGER_CONFIG
- **Edit LETTER_POSITIONS**: Send new positions in the format:
  ```
  A:1,2,3;B:4,5,6
  ```
  This will update only the specified letters.
- **Edit WORD_LIST**: Send new words in the format:
  ```
  word1 word2;word3 word4
  ```
  Each `;` represents a new line.

## Installation on Raspberry Pi

To deploy this project on a Raspberry Pi:

### Step 0: Install git
1. SSH into your Raspberry Pi:
```bash
ssh pi@<RPI_IP_ADDRESS>
```
2. Install git:
```bash
sudo apt-get update
sudo apt-get install git
```
3. Clone the repository:
```bash
git clone <REPOSITORY_URL>
cd stranger-lights
```

### Step 2: Run the Setup Script

1. Make the setup script executable:
```bash
chmod +x setup.sh
```
2. Run the setup script:
```bash
./setup.sh
```
This will:
- Install all required dependencies.
- Configure the application to run automatically on system boot.
- Start the application immediately.

### Step 3: Verify the Service
Check that the service is running:
```bash
sudo systemctl status stranger-lights.service
```
To view logs:
```bash
sudo journalctl -u stranger-lights.service -f
```

## Development Notes

### Adding New Routines
1. Create a new function for the routine in the appropriate module.
2. Add the routine to the `ROUTINES` dictionary in `main.py`:
   ```python
   ROUTINES = {
       "test_routine": test_routine,
       "portal_routine": portal_routine,
       "stranger_routine": stranger_routine,
       "christmas_routine": christmas_routine,
       "new_routine": new_routine
   }
   ```
3. Add the routine in the Telegram bot command handler:
    ```python
    routines = ["test_routine", "portal_routine", "stranger_routine", "christmas_routine"]
    ```

### Error Handling
- Errors are logged to the console.
- The Telegram bot provides user-friendly error messages for invalid inputs or formatting issues.

## Testing
- Use mock mode (`USE_MOCK = true`) to simulate NeoPixel behavior without hardware.
- Verify Telegram bot functionality by sending commands and checking updates to `config.json`.

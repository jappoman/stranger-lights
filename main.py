import json
import time
import threading
from lib.utility import *
from lib.portal import portal_routine
from lib.test import test_routine
from lib.stranger import stranger_routine
from lib.christmas import christmas_routine
from telegrambot import run_telegram_bot

# Function to load configuration dynamically
def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

# Map routine names to actual functions
ROUTINES = {
    "test_routine": test_routine,
    "portal_routine": portal_routine,
    "stranger_routine": stranger_routine,
    "christmas_routine": christmas_routine,
}

# Load initial configuration
config = load_config()

# Initialize NeoPixel or mock based on the configuration
neopixel_config = config["NEOPIXEL_CONFIG"]
if config["USE_MOCK"]:
    from lib.mock_neopixel import NeoPixel
    PIXEL_PIN = neopixel_config["PIXEL_PIN"]  # Mock doesn't use a real PIN
else:
    import board
    import neopixel
    PIXEL_PIN = getattr(board, neopixel_config["PIXEL_PIN"])  # Map string to board attribute dynamically

# Common configuration
NUM_PIXELS = neopixel_config["NUM_PIXELS"]
BRIGHTNESS = neopixel_config["BRIGHTNESS"]
AUTO_WRITE = neopixel_config["AUTO_WRITE"]
ORDER = getattr(neopixel, neopixel_config["ORDER"]) if not config["USE_MOCK"] else neopixel_config["ORDER"]

# Initialize NeoPixel or mock with the loaded configuration
pixels = NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=AUTO_WRITE, pixel_order=ORDER
)

# Main Program
if __name__ == "__main__":
    turn_off(pixels)
    last_routine = None

    # Avvia il bot Telegram in un thread separato
    bot_thread = threading.Thread(target=run_telegram_bot, daemon=True)
    bot_thread.start()

    while True:
        try:
            # Reload configuration dynamically
            config = load_config()

            # Get the routine to execute
            routine_name = config.get("ROUTINE", "")
            if routine_name != last_routine:
                print(f"Switching to routine: {routine_name}")
                last_routine = routine_name

            # Get the routine function
            routine = ROUTINES.get(routine_name)
            if routine:
                routine(pixels)
            else:
                print(f"Unknown routine: {routine_name}")

        except Exception as e:
            print(f"Error: {e}")

        # Sleep for a short period to avoid excessive file access
        time.sleep(1)

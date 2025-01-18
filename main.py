import importlib
import json
import time
import threading
from lib.utility import turn_off
from telegrambot import run_telegram_bot
import board
import neopixel


# Function to load configuration dynamically
def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)


# Function to dynamically load routines from config
def load_routines_from_config():
    config = load_config()
    routine_list = config.get("ROUTINE_LIST", [])
    routines = {}
    for routine in routine_list:
        try:
            module = importlib.import_module(routine["module"])
            routines[routine["name"]] = getattr(module, routine["name"])
        except (ImportError, AttributeError) as e:
            print(f"Error loading routine {routine['name']}: {e}")
    return routines


# Initialize NeoPixel or mock based on the configuration
def initialize_pixels(config):
    neopixel_config = config["NEOPIXEL_CONFIG"]
    if config["USE_MOCK"]:
        from lib.mock_neopixel import NeoPixel
        return NeoPixel(
            neopixel_config["PIXEL_PIN"],
            neopixel_config["NUM_PIXELS"],
            brightness=neopixel_config["BRIGHTNESS"],
            auto_write=neopixel_config["AUTO_WRITE"],
            pixel_order=neopixel_config["ORDER"]
        )
    else:
        pixel_pin = getattr(board, neopixel_config["PIXEL_PIN"], None)
        if not pixel_pin:
            raise AttributeError(f"Invalid GPIO pin: {neopixel_config['PIXEL_PIN']}")

        return neopixel.NeoPixel(
            pixel_pin,
            neopixel_config["NUM_PIXELS"],
            brightness=neopixel_config["BRIGHTNESS"],
            auto_write=neopixel_config["AUTO_WRITE"],
            pixel_order=getattr(neopixel, neopixel_config["ORDER"], neopixel.RGB)
        )


# Function to handle the light routines in a separate thread
def run_light_routines():
    config = load_config()
    ROUTINES = load_routines_from_config()
    pixels = initialize_pixels(config)

    turn_off(pixels)
    last_routine = None

    while True:
        try:
            # Reload configuration dynamically
            config = load_config()

            # Get the routine to execute
            routine_name = config.get("ROUTINE", "")
            if routine_name != last_routine:
                print(f"Switching to routine: {routine_name}")
                last_routine = routine_name

            # Execute the routine
            routine = ROUTINES.get(routine_name)
            if routine:
                routine(pixels)
            else:
                print(f"Unknown routine: {routine_name}")

        except Exception as e:
            print(f"Error in light routine: {e}")

        # Sleep to reduce file access frequency
        time.sleep(1)


# Main Program
if __name__ == "__main__":
    # Start the light routines in a separate thread
    light_thread = threading.Thread(target=run_light_routines, daemon=True)
    light_thread.start()

    # Run the Telegram bot in the main thread
    run_telegram_bot()

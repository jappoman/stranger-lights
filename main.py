import json
from lib.generic import *
from lib.portal import *
#from lib.stranger import *

# Load configuration from file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Determine whether to use the mock or the real NeoPixel library
if config["USE_MOCK"]:
    from lib.mock_neopixel import NeoPixel
    PIXEL_PIN = config["PIXEL_PIN"]  # Il mock non usa PIN reale
else:
    import board
    import neopixel
    PIXEL_PIN = getattr(board, config["PIXEL_PIN"])  # Map string to board attribute dynamically

# Common configuration
NUM_PIXELS = config["NUM_PIXELS"]
BRIGHTNESS = config["BRIGHTNESS"]
AUTO_WRITE = config["AUTO_WRITE"]
ORDER = getattr(neopixel, config["ORDER"]) if not config["USE_MOCK"] else config["ORDER"]

# Initialize NeoPixel or mock with the loaded configuration
pixels = NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=AUTO_WRITE, pixel_order=ORDER
)

# Main Program
if __name__ == "__main__":
    turn_off(pixels)

    while True:
        orange_portal(pixels)
        blue_portal(pixels)

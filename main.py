# Refactored lights.py
import time
import random
import board
import neopixel

# Configuration for NeoPixel
PIXEL_PIN = board.D18  # Pin connected to NeoPixel Data In
NUM_PIXELS = 100       # Number of NeoPixels
ORDER = neopixel.RGB   # Pixel color order

pixels = neopixel.NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# Main Program
if __name__ == "__main__":
    init_pixels()

    while True:
        init_pixels()
        orange_portal()
        init_pixels()
        blue_portal()

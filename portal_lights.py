# Refactored portal_lights.py
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

# Utility Functions
def init_pixels():
    """Turn off all pixels."""
    pixels.fill((0, 0, 0))
    pixels.show()

def portal_effect(color_range, direction='forward', cycles=100):
    """Create a portal-like effect with rotating colors."""
    colors = [(random.randint(*color_range[0]), random.randint(*color_range[1]), random.randint(*color_range[2]))
              for _ in range(NUM_PIXELS)]

    for _ in range(cycles):
        if direction == 'forward':
            first_pixel = colors.pop(0)
            colors.append(first_pixel)
        else:
            last_pixel = colors.pop()
            colors.insert(0, last_pixel)
        for i, color in enumerate(colors):
            pixels[i] = color
        pixels.show()
        time.sleep(0.03)

def orange_portal():
    """Display an orange portal effect."""
    portal_effect(((120, 180), (40, 70), (0, 0)), direction='forward')

def blue_portal():
    """Display a blue portal effect."""
    portal_effect(((0, 0), (30, 100), (120, 250)), direction='backward')

# Main Program
if __name__ == "__main__":
    init_pixels()

    while True:
        init_pixels()
        orange_portal()
        init_pixels()
        blue_portal()

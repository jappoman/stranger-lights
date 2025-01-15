import time
import random
from lib.utility import turn_off

def _wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def _rainbow_cycle(pixels, wait):
    """Display a rainbow cycle across all pixels."""
    num_pixels = len(pixels)
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = _wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def light_sequence(pixels, reverse=False):
    """Sequentially light up all pixels."""
    num_pixels = len(pixels)
    pixel_range = range(num_pixels - 1, -1, -1) if reverse else range(num_pixels)
    turn_off(pixels)
    for i in pixel_range:
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(0.1)

def random_lights(pixels, cycles=4):
    """Display random colors across all pixels."""
    num_pixels = len(pixels)
    for _ in range(cycles):
        for i in range(num_pixels):
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(1)

def christmas_routine(pixels):
    light_sequence(pixels)
    random_lights(pixels)
    _rainbow_cycle(pixels, 0.01)
    random_lights(pixels)
    light_sequence(pixels, reverse=True)
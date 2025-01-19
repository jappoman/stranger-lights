import time
import random
from lib.utility import turn_off

def _test_pixels(pixels):
    """Test each pixel with random colors."""
    num_pixels = len(pixels)
    for i in range(num_pixels):
        pixels.fill((0, 0, 0))
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(0.1)

def _light_sequence(pixels, reverse=False):
    """Sequentially light up all pixels."""
    num_pixels = len(pixels)
    pixel_range = range(num_pixels - 1, -1, -1) if reverse else range(num_pixels)
    turn_off(pixels)
    for i in pixel_range:
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(0.1)

def test_routine(pixels):
    """Run a test routine with random colors."""
    turn_off(pixels)
    _test_pixels(pixels)
    _light_sequence(pixels)

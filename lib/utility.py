import time
import random

def turn_off(pixels):
    """Turn off all pixels."""
    pixels.fill((0, 0, 0))
    pixels.show()

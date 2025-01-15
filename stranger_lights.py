# Refactored stranger_lights.py
import time
import random
import board
import neopixel

# Initialize the random seed
random.seed()

# Configuration for NeoPixel
PIXEL_PIN = board.D18  # Pin connected to NeoPixel Data In
NUM_PIXELS = 100       # Number of NeoPixels
ORDER = neopixel.RGB   # Pixel color order

pixels = neopixel.NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def init_pixels():
    """Turn off all pixels."""
    pixels.fill((0, 0, 0))
    pixels.show()

def test_pixels():
    """Test each pixel with random colors."""
    for i in range(NUM_PIXELS):
        pixels.fill((0, 0, 0))
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(0.1)
    init_pixels()

def light_sequence(reverse=False):
    """Sequentially light up all pixels."""
    pixel_range = range(NUM_PIXELS - 1, -1, -1) if reverse else range(NUM_PIXELS)
    init_pixels()
    for i in pixel_range:
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(0.1)
    time.sleep(1)

def random_lights(cycles=4):
    """Display random colors across all pixels."""
    for _ in range(cycles):
        for i in range(NUM_PIXELS):
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(1)

def fade_lights(cycles=3, fade_in=True):
    """Fade lights in or out with random colors."""
    for _ in range(cycles):
        if fade_in:
            init_pixels()
        for i in range(NUM_PIXELS):
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(random.uniform(0.5, 1.0))
        if not fade_in:
            init_pixels()

def spell_words(word_list, sleep_time=0.5):
    """Spell out words using predefined letter positions."""
    from letterlist import letter_positions

    for word in word_list:
        for char in word.upper():
            init_pixels()
            if char in letter_positions:
                for pos in letter_positions[char]:
                    pixels[pos] = (
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                    )
                pixels.show()
            time.sleep(sleep_time)
        time.sleep(sleep_time)

# Main Program
if __name__ == "__main__":
    init_pixels()

    while True:
        light_sequence()
        random_lights()
        fade_lights(fade_in=False)
        with open("wordslist.txt", "r") as word_file:
            words = [line.strip() for line in word_file]
        spell_words(words)
        fade_lights(fade_in=True)

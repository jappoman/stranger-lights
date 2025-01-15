import time
import random
import json
from lib.utility import turn_off
from lib.christmas import random_lights

# Initialize the random seed
random.seed()

def spell_words(pixels, word_list, sleep_time=0.5):
    """Spell out words using predefined letter positions."""

    # Load configuration from file
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    LETTER_POSITIONS = config["LETTER_POSITIONS"]

    for word in word_list:
        for char in word.upper():
            turn_off(pixels)
            if char in LETTER_POSITIONS:
                for pos in LETTER_POSITIONS[char]:
                    pixels[pos] = (
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                    )
                pixels.show()
            time.sleep(sleep_time)
        time.sleep(sleep_time)

def fade_lights(pixels, cycles=3, fade_in=True):
    """Fade lights in or out with random colors."""
    num_pixels = len(pixels)
    for _ in range(cycles):
        if fade_in:
            turn_off(pixels)
        for i in range(num_pixels):
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(random.uniform(0.5, 1.0))
        if not fade_in:
            turn_off(pixels)
    time.sleep(1)

def stranger_routine(pixels):
    random_lights(pixels)
    fade_lights(pixels, fade_in=False)
    with open("wordslist.txt", "r") as word_file:
        words = [line.strip() for line in word_file]
    spell_words(pixels, words)
    fade_lights(pixels, fade_in=True)

import time
import random
import json
from lib.utility import turn_off
from lib.christmas import random_lights

# Initialize the random seed
random.seed()

def spell_words(pixels, letter_positions, word_list, sleep_time=0.7):
    """Spell out words using predefined letter positions."""
    for word in word_list:
        for char in word.upper():
            turn_off(pixels)
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
    # Load configuration from file
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Retrieve the configuration for the stranger routine
    stranger_config = config.get("STRANGER_CONFIG", {})
    letter_positions = stranger_config.get("LETTER_POSITIONS", {})
    word_list = stranger_config.get("WORD_LIST", [])

    # Run the stranger routine
    random_lights(pixels)
    fade_lights(pixels, fade_in=False)
    spell_words(pixels, letter_positions, word_list)
    fade_lights(pixels, fade_in=True)

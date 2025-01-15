import time
import random

# Initialize the random seed
random.seed()

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

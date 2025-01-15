import time

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

def turn_off(pixels):
    """Turn off all pixels."""
    pixels.fill((0, 0, 0))
    pixels.show()

def rainbow_cycle(pixels, wait):
    """Display a rainbow cycle across all pixels."""
    num_pixels = len(pixels)
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = _wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

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

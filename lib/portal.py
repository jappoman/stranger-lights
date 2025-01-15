import time
import random

def _portal_effect(pixels, color_range, direction='forward', cycles=100):
    """Create a portal-like effect with rotating colors."""
    num_pixels = len(pixels)  # Determina il numero di pixel dinamicamente

    # Genera i colori iniziali
    colors = [(random.randint(*color_range[0]), random.randint(*color_range[1]), random.randint(*color_range[2]))
              for _ in range(num_pixels)]

    for _ in range(cycles):
        # Ruota i colori in avanti o indietro
        if direction == 'forward':
            first_pixel = colors.pop(0)
            colors.append(first_pixel)
        elif direction == 'backward':
            last_pixel = colors.pop()
            colors.insert(0, last_pixel)

        # Applica i colori ai pixel
        for i, color in enumerate(colors):
            pixels[i] = color
        pixels.show()
        time.sleep(0.03)

def _orange_portal(pixels):
    """Display an orange portal effect."""
    orange_color_range = ((120, 180), (40, 70), (0, 0))
    _portal_effect(pixels, orange_color_range, direction='forward', cycles=100)

def _blue_portal(pixels):
    """Display a blue portal effect."""
    blue_color_range = ((0, 0), (30, 100), (120, 250))
    _portal_effect(pixels, blue_color_range, direction='backward', cycles=100)

def _portal(pixels, color_range, direction='forward', cycles=100):
    """Display a portal effect with custom color range."""
    _portal_effect(pixels, color_range, direction, cycles)

def portal_routine(pixels):
    """Run a routine of portal effects."""
    for _ in range(2):
        _orange_portal(pixels)
        _blue_portal(pixels)
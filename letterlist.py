# Refactored letterlist.py
"""
This module defines letter positions on a NeoPixel grid. Each letter corresponds to a list of pixel indices.
"""

LETTER_POSITIONS = {
    'A': [73, 75, 76],
    'B': [71, 72],
    'C': [70],
    'D': [68],
    'E': [66, 67],
    'F': [64, 65],
    'G': [63],
    'H': [61, 62],
    'I': [60],
    'J': [58, 59],
    'K': [49, 50],
    'L': [48],
    'M': [46, 47],
    'N': [44, 45],
    'O': [43],
    'P': [40, 41],
    'Q': [39],
    'R': [37, 38],
    'S': [35],
    'T': [33, 34],
    'U': [31, 32],
    'V': [20, 21],
    'W': [17, 18, 19],
    'X': [16],
    'Y': [14],
    'Z': [11, 12]
}

if __name__ == "__main__":
    # Debug: Print all letter positions
    for letter, positions in LETTER_POSITIONS.items():
        print(f"{letter}: {positions}")

class NeoPixel:
    def __init__(self, pin, num_pixels, brightness=1.0, auto_write=True, pixel_order=None):
        self.num_pixels = num_pixels
        self.brightness = brightness
        self.auto_write = auto_write
        self.pixel_order = pixel_order
        self.pixels = [(0, 0, 0)] * num_pixels  # Simula i pixel come una lista di tuple RGB

    def __len__(self):
        return self.num_pixels

    def __setitem__(self, index, color):
        self.pixels[index] = color
        if self.auto_write:
            self.show()

    def __getitem__(self, index):
        return self.pixels[index]

    def fill(self, color):
        self.pixels = [color] * self.num_pixels
        if self.auto_write:
            self.show()

    def show(self):
        self._print_pixels()

    def _print_pixels(self):
        """Print the current state of pixels as colored asterisks."""
        print("\033[1A", end="")  # Move cursor up one line
        print("\033[2K", end="")  # Clear the current line
        for color in self.pixels:
            r, g, b = color
            print(self._rgb_to_ansi(r, g, b) + "*", end="")
        print("\033[0m", end="\r")  # Reset color and carriage return

    def _rgb_to_ansi(self, r, g, b):
        """Convert RGB values to ANSI color escape code."""
        return f"\033[38;2;{r};{g};{b}m"

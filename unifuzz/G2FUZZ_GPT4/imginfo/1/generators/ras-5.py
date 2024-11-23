from PIL import Image
import os

# Define the size of the image
width, height = 100, 100

# Create a new image with mode 'P' for palette-based
image = Image.new('P', (width, height))

# Define a simple color palette: red, green, blue, and black
palette = [
    255, 0, 0,   # Red
    0, 255, 0,   # Green
    0, 0, 255,   # Blue
    0, 0, 0      # Black
]

# Extend the palette to the required size
palette.extend(palette[-3:] * ((256 - len(palette) // 3)))

# Put the palette into the image
image.putpalette(palette)

# Fill the image in quarters with each color
for y in range(height):
    for x in range(width):
        if x < width // 2 and y < height // 2:
            color = 0  # Red
        elif x >= width // 2 and y < height // 2:
            color = 1  # Green
        elif x < width // 2 and y >= height // 2:
            color = 2  # Blue
        else:
            color = 3  # Black
        image.putpixel((x, y), color)

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image in a supported format (e.g., PNG)
image.save('./tmp/palette_image.png')
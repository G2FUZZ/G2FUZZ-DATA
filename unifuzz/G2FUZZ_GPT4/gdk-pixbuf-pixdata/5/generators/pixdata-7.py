from PIL import Image

# Define the size of the image
width, height = 100, 100

# Create a new image with mode 'P' for palette-based and the specified size
image = Image.new('P', (width, height))

# Define a palette: this is a sequence of RGB values
# Here, we define a simple 3-color palette (black, red, green).
# Each color is defined by its RGB components (Red, Green, Blue), with each component ranging from 0 to 255.
# Since the palette mode expects a sequence of 768 values (256 colors * 3), we fill the rest with zeros.
palette = [
    0, 0, 0,  # Black
    255, 0, 0,  # Red
    0, 255, 0,  # Green
] + [0] * (256-3) * 3  # Fill the rest of the palette with black

# Assign the palette to the image
image.putpalette(palette)

# Create pixel data that references the palette
# Each value in the pixel data corresponds to an index in the palette
# Here we create a pattern using the colors from our palette
for y in range(height):
    for x in range(width):
        if (x // 10) % 2 == (y // 10) % 2:
            image.putpixel((x, y), 1)  # Use the second color in the palette (Red)
        else:
            image.putpixel((x, y), 2)  # Use the third color in the palette (Green)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image.save('./tmp/pixdata_palette_image.png')
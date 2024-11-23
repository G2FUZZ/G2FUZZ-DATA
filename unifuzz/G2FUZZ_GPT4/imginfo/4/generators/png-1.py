from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image size
width, height = 800, 600

# Creating a new image with RGB mode
image = Image.new("RGB", (width, height))

# Generating a simple pattern
for x in range(width):
    for y in range(height):
        # Defining RGB values based on position to create a pattern
        r = (x % 256)  # Red varies with X
        g = (y % 256)  # Green varies with Y
        b = ((x + y) % 256)  # Blue varies with X+Y
        image.putpixel((x, y), (r, g, b))

# Save the image with lossless compression as a PNG
image.save('./tmp/lossless_compression_demo.png')
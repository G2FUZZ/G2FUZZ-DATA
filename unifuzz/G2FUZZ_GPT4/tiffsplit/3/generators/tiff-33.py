from PIL import Image
import numpy as np

# Create a gradient image (for example, 256x256 pixels)
width, height = 256, 256
# Creating an RGB image as before
image_rgb = Image.new("RGB", (width, height))

# Generate a gradient from top to bottom for RGB
for y in range(height):
    for x in range(width):
        image_rgb.putpixel((x, y), (int(x % 256), int(y % 256), 128))

# Now, creating a CMYK image
image_cmyk = Image.new("CMYK", (width, height))
# Generate a gradient from top to bottom for CMYK
for y in range(height):
    for x in range(width):
        # CMYK colors require a conversion from RGB
        c = 255 - int(x % 256)
        m = 255 - int(y % 256)
        yk = 128  # Just a constant value for demonstration
        k = 0     # Typically, you'll calculate this based on your requirements
        image_cmyk.putpixel((x, y), (c, m, yk, k))

# Creating a grayscale image
image_gray = Image.new("L", (width, height))
# Generate a gradient for grayscale
for y in range(height):
    for x in range(width):
        gray_value = int((x + y) / 2) % 256
        image_gray.putpixel((x, y), gray_value)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the RGB image as a TIFF with tiling
image_rgb.save('./tmp/gradient_rgb_tile.tiff', format='TIFF', tile=('tile', 128, 128))

# Save the CMYK image as a TIFF
image_cmyk.save('./tmp/gradient_cmyk_tile.tiff', 'TIFF')

# Save the grayscale image as a TIFF
image_gray.save('./tmp/gradient_gray_tile.tiff', 'TIFF')

print("TIFF images with multiple color spaces saved to ./tmp/")
from PIL import Image, ImageDraw
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with CMYK color mode
# For demonstration, we're creating an image of size 100x100
width, height = 100, 100
cmyk_color = (0, 0, 0, 0)  # Pure black in CMYK

# Create a new image with CMYK color mode
image = Image.new("CMYK", (width, height), cmyk_color)

# Simulating a spot color by filling part of the image with a specific CMYK value
# Let's say we want to simulate a spot color in a specific area of the image
draw = ImageDraw.Draw(image)
spot_color = (0, 255, 255, 0)  # A bright yellow-green-ish color in CMYK
draw.rectangle([25, 25, 75, 75], fill=spot_color)

# Save the image as TIFF
image.save('./tmp/spot_color_simulation.tiff')
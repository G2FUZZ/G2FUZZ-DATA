import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGBA (Red, Green, Blue, Alpha) mode for transparency
width, height = 400, 400
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))  # Fully transparent background

# Draw a semi-transparent square
for x in range(100, 300):
    for y in range(100, 300):
        image.putpixel((x, y), (255, 0, 0, 128))  # Semi-transparent red

# Save the image
image.save('./tmp/transparent_example.png')
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate and save 3 images with 24-bit color depth

# Image 1: Gradient
image1 = Image.new("RGB", (256, 256), "#FFFFFF")
for x in range(256):
    for y in range(256):
        image1.putpixel((x, y), (x, y, 128))
image1.save('./tmp/gradient.jpg')

# Image 2: Solid Color
image2 = Image.new("RGB", (256, 256), "#FF5733")
image2.save('./tmp/solid_color.jpg')

# Image 3: Random Pixels
import random
image3 = Image.new("RGB", (256, 256), "#FFFFFF")
for x in range(256):
    for y in range(256):
        image3.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
image3.save('./tmp/random_pixels.jpg')
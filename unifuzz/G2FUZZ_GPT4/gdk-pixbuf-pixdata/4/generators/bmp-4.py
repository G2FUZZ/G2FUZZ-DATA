from PIL import Image

# Create an empty image with RGBA mode (32-bit including alpha channel)
width, height = 200, 200
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Create a semi-transparent red square
for x in range(50, 150):
    for y in range(50, 150):
        image.putpixel((x, y), (255, 0, 0, 128))  # Red, Green, Blue, Alpha

# Ensure the ./tmp/ directory exists or create it
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the image
image.save('./tmp/transparent_image.bmp')
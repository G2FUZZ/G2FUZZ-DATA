from PIL import Image

# Create an RGBA image (Red, Green, Blue, Alpha)
width, height = 100, 100
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Draw a simple red square with transparency in the middle of the image
for x in range(25, 75):
    for y in range(25, 75):
        image.putpixel((x, y), (255, 0, 0, 128))  # Semi-transparent red

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as TGA
image.save('./tmp/example_with_alpha.tga')
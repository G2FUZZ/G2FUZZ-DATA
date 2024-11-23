from PIL import Image

# Create an image with RGBA mode (Red, Green, Blue, Alpha) for transparency
width, height = 100, 100
image = Image.new('RGBA', (width, height), (255, 0, 0, 0))  # Fully transparent image

# Draw a semi-transparent square in the middle
for x in range(25, 75):
    for y in range(25, 75):
        image.putpixel((x, y), (0, 255, 0, 128))  # Semi-transparent green

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
file_path = './tmp/pixdata.png'
image.save(file_path)

print(f"Image with alpha channel saved to {file_path}")
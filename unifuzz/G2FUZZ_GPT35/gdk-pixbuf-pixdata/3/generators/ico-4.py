import os
from PIL import Image

# Create a new RGBA image with transparency
img = Image.new('RGBA', (64, 64), (255, 255, 255, 0))

# Save the image as ICO file
img.save('./tmp/transparent_icon.ico')
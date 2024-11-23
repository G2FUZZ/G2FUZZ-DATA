import io
from PIL import Image

# Create a new RGBA image with transparency
img = Image.new('RGBA', (64, 64), (255, 0, 0, 0))  # Red color with 0 alpha (fully transparent)

# Save the image as ICO file
img.save('./tmp/transparency_icon.ico', format='ICO')
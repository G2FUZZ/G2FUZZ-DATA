import io
from PIL import Image

# Create a new RGBA image
image = Image.new('RGBA', (16, 16), color=(255, 0, 0, 255))

# Save the image as ICO file
image.save('./tmp/icon.ico')
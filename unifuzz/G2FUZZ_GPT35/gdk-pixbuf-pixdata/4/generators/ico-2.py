import io
from PIL import Image

# Create a new transparent image (100x100 pixels)
img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Save the image as an ICO file
img.save('./tmp/transparent_icon.ico')
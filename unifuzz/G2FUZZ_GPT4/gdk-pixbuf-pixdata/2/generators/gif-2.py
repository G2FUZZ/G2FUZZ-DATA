from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a new image with a palette mode ('P') using a limited color palette
image = Image.new('P', (100, 100))

# Define a simple palette: black, red, green, blue
# Each color is defined by its RGB components
palette = [
    0, 0, 0,  # black
    255, 0, 0,  # red
    0, 255, 0,  # green
    0, 0, 255   # blue
]

# Put the palette into the image
image.putpalette(palette)

# Draw some shapes on the image using the colors from the palette
draw = ImageDraw.Draw(image)
draw.rectangle([10, 10, 45, 45], fill=1)  # Red square
draw.rectangle([55, 10, 90, 45], fill=2)  # Green square
draw.rectangle([10, 55, 45, 90], fill=3)  # Blue square

# Save the image as a GIF
image.save('./tmp/palette_based_color.gif')
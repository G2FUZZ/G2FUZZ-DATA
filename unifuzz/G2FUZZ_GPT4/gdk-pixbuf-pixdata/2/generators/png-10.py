from PIL import Image, ImageDraw

# Define the size of the image
width, height = 200, 200

# Create a new image with a mode of 'P', which stands for palette
image = Image.new('P', (width, height), 'white')

# Define the palette: black, red, green, blue
# Each color is defined by three components (R, G, B)
palette = [
    0, 0, 0,       # black
    255, 0, 0,     # red
    0, 255, 0,     # green
    0, 0, 255      # blue
]

# Put the palette into the image
image.putpalette(palette)

# Draw some shapes to demonstrate the use of the palette
draw = ImageDraw.Draw(image)

# Draw a black rectangle
draw.rectangle([50, 50, 100, 100], fill=0)

# Draw a red circle
draw.ellipse([110, 50, 160, 100], fill=1)

# Draw a green triangle
triangle = [50, 150, 75, 110, 100, 150]
draw.polygon(triangle, fill=2)

# Draw a blue line
draw.line([110, 150, 160, 150], fill=3, width=10)

# Ensure the './tmp/' directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Save the image
image.save('./tmp/palette_based_image.png')

print('Image has been saved to ./tmp/palette_based_image.png')
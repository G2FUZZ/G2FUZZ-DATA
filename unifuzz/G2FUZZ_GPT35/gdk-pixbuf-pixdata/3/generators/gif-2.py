import os
from PIL import Image, ImageDraw

# Create a directory to store the generated gif files
os.makedirs('./tmp/', exist_ok=True)

# Define image size and color depth
width, height = 100, 100
color_depth = 256

# Create a new image with 8-bit color depth
image = Image.new("P", (width, height))

# Generate a color palette with 256 colors
palette = [i for i in range(256)] * 3
image.putpalette(palette)

# Draw a colorful pattern on the image
draw = ImageDraw.Draw(image)
draw.rectangle([0, 0, width, height], fill=128)
draw.rectangle([20, 20, width-20, height-20], fill=200)
draw.ellipse([40, 40, width-40, height-40], fill=50)

# Save the image as a gif file
image.save('./tmp/colorful_pattern.gif')

print("GIF file with 256-color depth generated successfully!")
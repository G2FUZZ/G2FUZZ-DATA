from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Define image size and color palette
width, height = 200, 200
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow

# Create a new image with mode 'P' for palette-based and the defined size
image = Image.new('P', (width, height))

# Define the palette
# Flatten the colors list and extend it to match 768 (256*3) values, as required by a palette
palette = sum(colors, ())
# If the palette has less than 256 colors, fill the rest with black
palette += (0, 0, 0) * (256 - len(colors))

image.putpalette(palette)

# Use ImageDraw to create simple shapes
draw = ImageDraw.Draw(image)

# Draw some shapes to demonstrate the use of the palette
draw.polygon([(50, 100), (150, 100), (100, 20)], fill=1)   # Triangle, Red
draw.rectangle([50, 120, 150, 170], fill=2)                # Rectangle, Green
draw.ellipse([120, 30, 170, 80], fill=3)                   # Ellipse, Blue

# Save the image
image.save('./tmp/palette_image.png')
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a custom gradient background
width, height = 200, 200
image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)

# Define a custom gradient background
for y in range(height):
    for x in range(width):
        r = int(255 * (x / width))
        g = int(255 * (y / height))
        b = int(255 * ((x + y) / (width + height)))
        draw.point((x, y), fill=(r, g, b))

# Draw custom shapes on the image
draw.rectangle([50, 50, 150, 150], fill=(255, 255, 255), outline=(0, 0, 0))
draw.ellipse([75, 75, 125, 125], fill=(0, 255, 0), outline=(255, 255, 255))

# Add text annotations to the image
annotations = [
    "Custom Shape 1: Rectangle at (50, 50) to (150, 150)",
    "Custom Shape 2: Ellipse at (75, 75) to (125, 125)"
]

font = ImageFont.load_default()
y_position = 10
for annotation in annotations:
    draw.text((10, y_position), annotation, fill='white', font=font)
    y_position += 20

# Save the image with annotations and custom quality settings
quality_settings = 95
image.save("./tmp/complex_image_extended.jpg", quality=quality_settings)
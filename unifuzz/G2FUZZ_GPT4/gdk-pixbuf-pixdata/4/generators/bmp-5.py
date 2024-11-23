import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument name here

# Create an image with RGB mode
width, height = 640, 480
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Create a simple pattern to demonstrate device independence
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black']

# Draw rectangles across the image
for i, color in enumerate(colors):
    draw.rectangle([i * (width // len(colors)), 0, (i + 1) * (width // len(colors)), height], fill=color)

# Save the image as BMP
image.save('./tmp/device_independence.bmp')

print("BMP image created successfully.")
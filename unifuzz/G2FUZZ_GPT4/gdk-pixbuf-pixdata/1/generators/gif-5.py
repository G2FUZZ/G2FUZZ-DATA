from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 300, 300
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw some shapes to demonstrate interlacing
colors = ["red", "green", "blue", "yellow", "purple"]
for i, color in enumerate(colors, start=1):
    draw.rectangle([50*i, 50, 50*i + 50, 100], fill=color)

# Save the image with interlacing
image.save('./tmp/interlaced_image.gif', 'GIF', interlace=True)
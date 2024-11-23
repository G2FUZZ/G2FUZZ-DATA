from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be included in the image
text = """
9. Extensibility: The BMP format is extensible, allowing for the definition of custom headers and additional color space information, making it possible to adapt the format for specialized uses.
"""

# Image size
width, height = 800, 600
background_color = (255, 255, 255)  # White background
text_color = (0, 0, 0)  # Black text

# Create a new image with white background
img = Image.new('RGB', (width, height), color=background_color)

# Initialize the drawing context
draw = ImageDraw.Draw(img)

# Use a truetype font
try:
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    font = ImageFont.load_default()

# Prepare text wrapping
lines = textwrap.wrap(text, width=70)

# Starting position for the text
x, y = 50, 50

# Draw the text on the image
for line in lines:
    draw.text((x, y), line, font=font, fill=text_color)
    y += 15  # Move downward for the next line

# Save the image
img.save('./tmp/extensibility.bmp')
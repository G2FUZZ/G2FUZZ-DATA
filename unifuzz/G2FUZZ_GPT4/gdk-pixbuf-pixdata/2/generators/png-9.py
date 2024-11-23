import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Text to be drawn
text = """
9. Robustness: The PNG file format includes a CRC (Cyclic Redundancy Check) for the data in each chunk to ensure the integrity of the data during transfer. This makes PNG files more robust against file corruption compared to other image formats.
"""

# Creating a new image with white background
image = Image.new('RGB', (800, 200), color = 'white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Use a truetype font
try:
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    # Fallback to a default font if the preferred font is not available
    font = ImageFont.load_default()

# Position for the text
position = (10, 10)

# Adding text to image
draw.text(position, text, fill="black", font=font)

# Save the image
image.save('./tmp/robustness_png.png')
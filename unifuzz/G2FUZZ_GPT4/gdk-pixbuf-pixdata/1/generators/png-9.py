import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (600, 100), color='white')

# Initialize ImageDraw
draw = ImageDraw.Draw(img)

# Define text to draw
text = "9. Robust Error Detection: PNG uses CRC for detecting errors in the file, ensuring file integrity."

# Load a font
font = ImageFont.load_default()

# Calculate text width and height
text_width, text_height = draw.textsize(text, font=font)

# Calculate position for centered text
x = (img.width - text_width) / 2
y = (img.height - text_height) / 2

# Add text to image
draw.text((x, y), text, fill="black", font=font)

# Save the image
img.save('./tmp/robust_error_detection.png')
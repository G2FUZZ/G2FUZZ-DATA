import os
from PIL import Image, ImageDraw, ImageFont

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (600, 100), color = (255, 255, 255))

d = ImageDraw.Draw(img)

# Use a basic font and specify text
try:
    # Trying to use a nicer, default font if available on the system for better look
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    # Fallback to the default PIL font if specific fonts are not found
    font = ImageFont.load_default()

text = """
10. Robust Error Detection: PNG uses CRC (Cyclic Redundancy Check) for detecting corruption in the file. This ensures the integrity of the image data and helps in error detection when the file is transmitted over a network.
"""

# Add the text to the image
d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image as PNG
img.save('./tmp/robust_error_detection.png')
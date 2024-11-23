import os
from PIL import Image, ImageDraw, ImageFont

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 200), color='white')

# Initialize ImageDraw
d = ImageDraw.Draw(img)

# Adding text to image
text = """
8. Robust Error Detection: PNG uses CRC (Cyclic Redundancy Check) for detecting errors in the file data, 
ensuring the integrity of the file during transfer over networks or between storage devices.
"""

# Attempt to use a default font
try:
    # For better appearance on various systems, try to find a commonly available font
    font = ImageFont.truetype("arial.ttf", 15)
except IOError:
    # Fallback to default font if specific font not found
    font = ImageFont.load_default()

d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image
file_path = './tmp/robust_error_detection.png'
img.save(file_path)

print(f"Image saved at {file_path}")
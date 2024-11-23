import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with white background
img = Image.new('RGB', (600, 100), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Load a font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 14)

# Insert text
text = "8. Robust Error Detection: PNG files include a CRC (Cyclic Redundancy Check) for each chunk of data, ensuring high integrity and detection of any data corruption."
d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image as a PNG file
img.save('./tmp/error_detection_png.png')
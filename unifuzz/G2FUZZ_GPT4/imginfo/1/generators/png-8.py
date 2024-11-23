import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the text and file path
text = "8. Robust Error Detection: PNG uses CRC (Cyclic Redundancy Check) for error checking in file structure, enhancing file integrity during transfer or storage."
file_path = './tmp/robust_error_detection.png'

# Create an image with white background
img = Image.new('RGB', (800, 200), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Try to use a TTF font available from matplotlib, or default to PIL's basic font
try:
    font_path = f"{matplotlib.get_data_path()}/fonts/ttf/DejaVuSans.ttf"
    font = ImageFont.truetype(font_path, 14)
except Exception:
    font = ImageFont.load_default()

# Add text to the image
d.text((10,10), text, fill=(0,0,0), font=font)

# Save the image
img.save(file_path)

print(f"Image saved to {file_path}")
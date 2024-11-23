import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the resolution information (DPI)
resolution_info = (300, 300)  # 300x300 DPI

# Create an empty (black) image of 100x100 pixels
img = Image.new('RGB', (100, 100), color='black')

# Save the image with resolution information
img.save('./tmp/pixdata_with_resolution_info.jpg', dpi=resolution_info)
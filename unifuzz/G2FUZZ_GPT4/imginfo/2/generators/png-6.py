from PIL import Image, PngImagePlugin
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'blue')

# Prepare metadata
meta_info = PngImagePlugin.PngInfo()
meta_info.add_text("Author", "John Doe")
meta_info.add_text("Description", "This is a sample PNG image with metadata.")
meta_info.add_text("Creation Time", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Save the image with metadata into ./tmp/ directory
img.save('./tmp/sample_image_with_metadata.png', "PNG", pnginfo=meta_info)

print("Image with metadata saved successfully.")
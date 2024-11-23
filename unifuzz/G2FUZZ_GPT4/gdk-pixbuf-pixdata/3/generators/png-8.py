from PIL import Image, PngImagePlugin
import os
from datetime import datetime

# Create a directory for storing the generated PNG file if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple image
img = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Prepare metadata
meta = PngImagePlugin.PngInfo()
meta.add_text("Description", "This is a sample PNG image with metadata.")
meta.add_text("Author", "Generated by Python Script")
meta.add_text("Creation Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# Note: Modification time will be the time file was last modified, automatically set by the file system

# Save the image with metadata
file_path = os.path.join(output_dir, 'sample_image_with_metadata.png')
img.save(file_path, "PNG", pnginfo=meta)

print(f"Image saved to {file_path}")
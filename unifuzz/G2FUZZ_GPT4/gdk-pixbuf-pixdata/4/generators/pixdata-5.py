from PIL import Image, PngImagePlugin
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'blue')

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Creator", "Your Name")
metadata.add_text("Creation Date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
metadata.add_text("Copyright", "Copyright 2023 Your Name")
metadata.add_text("Description", "This is an example image with metadata.")

# Save the image with metadata
img.save('./tmp/example_pixdata.png', "PNG", pnginfo=metadata)
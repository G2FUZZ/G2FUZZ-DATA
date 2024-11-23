import os
from PIL import Image, PngImagePlugin

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'blue')

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Copyright", "Copyright © 2023 by My Company")
metadata.add_text("Author", "John Doe")
metadata.add_text("Description", "This is a sample image with metadata.")

# Save the image with metadata
img.save('./tmp/sample_with_metadata.png', "PNG", pnginfo=metadata)
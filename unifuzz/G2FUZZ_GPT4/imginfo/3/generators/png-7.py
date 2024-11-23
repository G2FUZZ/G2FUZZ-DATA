import os
from PIL import Image, PngImagePlugin

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'blue')

# Prepare metadata
meta_info = PngImagePlugin.PngInfo()
meta_info.add_text("Title", "Sample Image")
meta_info.add_text("Author", "Jane Doe")
meta_info.add_text("Copyright", "Copyright 2023 Jane Doe")
meta_info.add_text("Description", "This is an example of adding metadata to a PNG file.")

# Save the image with metadata
img.save('./tmp/sample_with_metadata.png', "PNG", pnginfo=meta_info)
from PIL import Image, PngImagePlugin
import os

# Create the /tmp directory if it doesn't already exist
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using PIL
img = Image.new('RGB', (100, 100), color = 'blue')

# Prepare some metadata to add to the PNG
meta_info = PngImagePlugin.PngInfo()

# Adding various pieces of metadata
meta_info.add_text("Description", "This is a sample PNG image with metadata.")
meta_info.add_text("Author", "John Doe")
meta_info.add_text("Copyright", "Copyright 2023 John Doe")
meta_info.add_text("Timestamp", "2023-01-01T12:00:00")

# Save the image with metadata
img.save('./tmp/sample_with_metadata.png', pnginfo=meta_info)
from PIL import Image, PngImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode and white background
img = Image.new('RGB', (100, 100), 'white')

# Metadata to insert
metadata = PngImagePlugin.PngInfo()
metadata.add_text("Description", "This is an example PNG image with metadata.")
metadata.add_text("Creation Time", "2023-10-01T12:00:00")
metadata.add_text("Software", "Generated using Pillow in Python")

# Save the image with metadata
img.save('./tmp/example_with_metadata.png', "PNG", pnginfo=metadata)
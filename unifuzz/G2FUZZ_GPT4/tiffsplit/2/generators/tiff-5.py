from PIL import Image, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image (for example: 100x100 pixels, black)
img = Image.new('RGB', (100, 100), color = 'black')

# Prepare some metadata
info = TiffImagePlugin.ImageFileDirectory_v2()

# Assign metadata using the correct numerical tag values
info[315] = 'John Doe'  # Artist
info[270] = 'Example TIFF image with metadata'  # ImageDescription
info[305] = 'Pillow'  # Software

# Save the image as TIFF with metadata
img.save('./tmp/example_with_metadata.tiff', tiffinfo=info)
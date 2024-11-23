from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Prepare metadata
info = TiffImagePlugin.ImageFileDirectory_v2()

# Example metadata fields
# Removed manual setting of ImageWidth and ImageLength as they are not necessary
info[282] = (96, 1)  # XResolution tag number is 282
info[283] = (96, 1)  # YResolution tag number is 283
info[296] = 2  # ResolutionUnit tag number is 296, 2 stands for inches
info[270] = 'Copyright 2023, Example Corp.'  # 270 is the tag for ImageDescription

# Save the TIFF with metadata
image.save('./tmp/example_with_metadata.tif', tiffinfo=info)
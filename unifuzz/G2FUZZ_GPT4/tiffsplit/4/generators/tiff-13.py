from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")

# Define custom tags in a dictionary
# Example of a custom tag: (tag_id, tag_type, length, value, writeonce)
# Refer to TIFF specification for tag_type constants
# This is a fictional example for demonstration; adjust tag IDs and types according to real needs
custom_tags = {
    700: (TiffTags.FLOAT, 1, (1.0,), False),  # Example custom tag for demo purposes
}

# Prepare the info dictionary to include custom tags
info = {
    "tile": ('raw', (256, 256)),
    "compression": "tiff_deflate",  # Use deflate compression; adjust as needed
}

# Add custom tags to the TIFF saving options
if hasattr(TiffImagePlugin, 'WRITE_LIBTIFF'):
    TiffImagePlugin.WRITE_LIBTIFF = True
info['custom'] = [(tag, value[0], value[1], value[2], value[3]) for tag, value in custom_tags.items()]

# Save the image, including custom tags, to a TIFF file
image.save('./tmp/tiled_image_with_custom_tags.tiff', format='TIFF', save_all=True, **info)

print("TIFF image with tiles and custom tags saved successfully.")
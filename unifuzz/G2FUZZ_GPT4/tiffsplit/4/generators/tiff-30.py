from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")

# Define custom tags in a dictionary
# Adding an 'Image Acquisition Data' tag (fictional example, adjust tag ID/type as needed)
custom_tags = {
    700: (TiffTags.FLOAT, 1, (1.0,), False),  # Previous custom tag example
    701: (TiffTags.ASCII, len("AcquisitionData"), ("AcquisitionData",), False)  # Image Acquisition Data
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
image.save('./tmp/tiled_image_with_custom_and_acquisition_tags.tiff', format='TIFF', save_all=True, **info)

print("TIFF image with tiles, custom, and Image Acquisition Data tags saved successfully.")
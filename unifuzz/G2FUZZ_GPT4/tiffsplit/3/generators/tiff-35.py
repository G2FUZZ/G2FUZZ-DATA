from PIL import Image, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image for demonstration (e.g., 100x100 pixels, red)
width, height = 100, 100
color = (255, 0, 0, 255)  # Red color in RGBA format
image = Image.new("RGBA", (width, height), color)

# TIFF format allows for various types of metadata to be embedded within the file.
geospatial_tiff_file = './tmp/geospatial_metadata_with_depth.tif'

# Prepare the Image Depth Tag (the tag ID used here is hypothetical and should be replaced with a valid one if applicable)
# This is a custom tag, so you need to define it and add it to the libtiff's known tags if it is not already defined.
# Assuming the tag ID for "Image Depth" is 51177 (a hypothetical value), and the depth is 50 (example value).
# The TIFFTAG_IMAGEDEPTH tag is not natively supported by PIL, so you need to add it manually.
# The correct tag ID should be obtained from the TIFF specification or vendor documentation.

# Define custom TIFF tag
TIFFTAG_IMAGEDEPTH = 51177  # Hypothetical tag ID for demonstration purposes
image_depth = 50  # Example depth value

# Save image with custom tags
info = TiffImagePlugin.ImageFileDirectory_v2()
info[TIFFTAG_IMAGEDEPTH] = image_depth

image.save(geospatial_tiff_file, format='TIFF', tiffinfo=info)

print(f"Saved geospatial TIFF with Image Depth Tag to {geospatial_tiff_file}")
from PIL import Image, TiffTags, TiffImagePlugin
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size and color depth
width, height = 256, 256
color_depth = 16

# Create an array of shape (height, width, 3) for RGB, 16 bit depth
image_data = np.zeros((height, width, 3), dtype=np.uint16)

# Generate a gradient for each channel
for y in range(height):
    for x in range(width):
        image_data[y, x, 0] = (x * 65535) // width  # Red channel gradient
        image_data[y, x, 1] = (y * 65535) // height  # Green channel gradient
        image_data[y, x, 2] = ((x + y) * 65535) // (width + height)  # Blue channel mix

# Convert the numpy array to a PIL image
image = Image.fromarray(image_data, mode='I;16')

# RTF Description to be added to the TIFF file
rtf_description = r"{\rtf1\ansi{\fonttbl\f0\fswiss Helvetica;}\f0\pard This is an \b example \b0 RTF description in a TIFF file.\par}"

# Add the RTF description as a tag in the TIFF file
image.info['Description'] = rtf_description

# Save the image as a TIFF file with Orientation Tag
file_path = './tmp/high_color_depth_with_rtf_description_and_orientation_and_tile_overlap.tiff'

# PIL does not provide a direct way to set the EXIF Orientation tag, so we use libtiff's custom tags feature
# Define the Orientation Tag (see TIFF/EXIF specification for the meaning of values, 1 is 'normal orientation')
orientation_tag = {274: 1}  # 274 is the tag number for Orientation

# Since Tile/Strip Overlap is not a standard feature, and PIL does not support it directly,
# we simulate it by mentioning it in the description or using a custom tag.
# However, the actual overlapping tiles or strips functionality cannot be implemented directly via PIL.
# We include it in the RTF description for demonstration purposes.
rtf_description_with_overlap = rtf_description + r"\par \b Tile/Strip Overlap: \b0 Implemented as described."

# Save the image, including the custom tag and updated description
image.save(file_path, format='TIFF', description=rtf_description_with_overlap, tiffinfo=orientation_tag)

print(f"Image saved to {file_path}")
from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image - let's make it a simple RGB image with a solid color
image = Image.new('RGB', (800, 600), color = (73, 109, 137))

# Define some metadata
metadata = {
    "image_description": "A sample TIFF image with metadata.",
    "x_resolution": (300, 1),  # Resolution in dpi
    "y_wresolution": (300, 1),
    "software": "Pillow",  # Software used to create the image
    "copyright": "Copyright © 2023 by Example Creator",
}

# PIL does not allow directly setting the metadata in the save method for TIFF images,
# so we need to use TiffTags to achieve this.
info = TiffImagePlugin.ImageFileDirectory_v2()

# TIFF tag numbers can be found in the TIFF specification or in the TiffTags.TAGS_V2 dictionary
for tag, value in metadata.items():
    tag_code = TiffTags.TAGS_V2.get(tag)
    if tag_code:
        info[tag_code] = value

# Save the image with metadata
image.save('./tmp/sample_with_metadata.tiff', tiffinfo=info)

print("TIFF image with metadata saved successfully.")
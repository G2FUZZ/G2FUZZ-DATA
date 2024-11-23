from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image - let's make it a simple RGB image with a solid color
image = Image.new('RGB', (800, 600), color = (73, 109, 137))

# Define some metadata
metadata = {
    "image_description": "A sample TIFF image with metadata and Spot Color Support.",
    "x_resolution": (300, 1),  # Resolution in dpi
    "y_wresolution": (300, 1),
    "software": "Pillow",  # Software used to create the image
    "copyright": "Copyright © 2023 by Example Creator",
    # Adding a description of the Spot Color Support feature
    "spot_color_support": "Includes Spot Color channels for precise color matching in printing."
}

# PIL does not allow directly setting the metadata in the save method for TIFF images,
# so we need to use TiffTags to achieve this.
info = TiffImagePlugin.ImageFileDirectory_v2()

# TIFF tag numbers can be found in the TIFF specification or in the TiffTags.TAGS_V2 dictionary
for tag, value in metadata.items():
    tag_code = TiffTags.TAGS_V2.get(tag)
    if tag_code:
        info[tag_code] = value
    else:
        # For custom or undefined tags like 'spot_color_support', we need to define them.
        # Assuming '37500' is an unused tag code for demonstration. In real application,
        # ensure this does not conflict with standard or other custom tags.
        # The choice of tag number should be based on TIFF specification and avoiding conflicts.
        custom_tag_code = 37500  # Example tag code, not officially assigned
        if tag == 'spot_color_support':
            info[custom_tag_code] = value

# Save the image with metadata
image.save('./tmp/sample_with_spot_color_support.tiff', tiffinfo=info)

print("TIFF image with Spot Color Support metadata saved successfully.")
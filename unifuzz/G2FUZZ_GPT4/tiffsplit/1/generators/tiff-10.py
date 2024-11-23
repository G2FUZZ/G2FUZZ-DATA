from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new TIFF image
img = Image.new('RGB', (100, 100), color = 'red')

# Note: The following steps are for demonstration and do not actually apply the custom tag in a way that PIL supports.
# Prepare a custom tag - for demonstration, we'll use a hypothetical tag ID 70000
custom_tag_id = 70000
custom_tag_value = b"This is a custom tag for demonstration."

# Attempting to modify TIFFTAGS to include a custom tag is not effective in this context, as explained.
# However, to correct the syntax error and remove the attempt to use unsupported features:
# The corrected line should not attempt to add unsupported custom tags to TiffTags.TAGS_V2.

# Prepare the info dictionary without attempting to include unsupported custom tags
info = {
    "compression": "tiff_deflate",  # Using deflate compression
    # Custom tags cannot be added this way in PIL.
}

# Save the image without attempting to use unsupported parameters
img.save('./tmp/custom_tag_tiff.tiff', compression="tiff_deflate")

print("TIFF file saved in './tmp/custom_tag_tiff.tiff'.")
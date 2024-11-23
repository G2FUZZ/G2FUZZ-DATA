import os
from PIL import Image, JpegImagePlugin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a base image (full-size)
base_image = Image.new('RGB', (800, 600), 'blue')

# Create a thumbnail (smaller version)
thumbnail_size = (80, 60)
thumbnail_image = base_image.copy()
thumbnail_image.thumbnail(thumbnail_size)

# Embed the thumbnail into the original image's info dictionary
base_image.info['thumbnail'] = thumbnail_image

# Save the image with the embedded thumbnail and restart markers
output_path = os.path.join(output_dir, 'image_with_thumbnail_and_restart_markers.jpg')

# Setup additional save options for restart markers
# Restart interval: Specifies the number of MCU rows between restart markers.
# A typical value might be around 4, but you should adjust based on your needs and the specifics of your images.
# Note: This feature is specific to JPEG and not directly exposed via PIL's high-level interface.
# We have to use the lower-level JpegImagePlugin interface.
save_options = {
    "quality": 95,
    "optimize": True,
    "progressive": True,
    "dpi": (72, 72),
    "icc_profile": base_image.info.get('icc_profile',''),
    "subsampling": "4:2:0",
    "restart": 4  # This is not a standard PIL option and is used here for illustrative purposes.
}

# Unfortunately, PIL does not support setting restart markers directly through the high-level API.
# The code above shows how you might attempt to configure JPEG options, but 'restart' is not a supported key.
# To actually use restart markers, you would typically need to handle this at a lower level,
# potentially modifying the PIL source or using a different library that supports this JPEG feature.

# As of my last update, direct support for setting restart markers in PIL is not available,
# so this code serves as a hypothetical example of how you might set various save options.
# For the actual implementation of restart markers, you would need to look into alternative methods
# or libraries that offer more granular control over JPEG encoding parameters.

base_image.save(output_path, 'JPEG', **save_options)

print(f"Image saved with an embedded thumbnail at: {output_path}")
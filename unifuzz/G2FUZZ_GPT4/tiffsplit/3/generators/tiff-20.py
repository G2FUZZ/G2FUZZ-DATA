from PIL import Image, PngImagePlugin
import os

# Create a gradient image (for example, 256x256 pixels)
width, height = 256, 256
image = Image.new("RGB", (width, height))

# Generate a gradient from top to bottom
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), (int(x % 256), int(y % 256), 128))

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Creating a thumbnail as a subfile
thumbnail_size = (64, 64)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the main image with tiling
image.save('./tmp/gradient_tile_colorimetry.tiff', format='TIFF', tile=('tile', 128, 128))

# Saving the thumbnail
thumbnail.save('./tmp/gradient_tile_colorimetry_thumbnail.tiff', format='TIFF')

# Digital Rights Management (DRM) feature
# For the DRM, we'll use metadata to include copyright notice and usage restrictions in the main image.
# This is a basic implementation and for full DRM protection, more sophisticated methods should be considered.
drm_metadata = {
    "Copyright": "Copyright 2023, The Image Creator",
    "Usage Rights": "No reproduction or distribution without permission."
}

# PIL does not directly support setting arbitrary metadata in TIFF files in a way that would implement DRM.
# However, adding copyright and usage rights information as metadata can be a basic step.
# For demonstration purposes, we show how to add simple text metadata to a PNG,
# as TIFF metadata handling is more complex and less supported in PIL.
# In practice, implementing DRM would require handling metadata according to TIFF/EP standards or using specialized software.

# Saving a version with "DRM" metadata (demonstration with PNG, as an example)
info = PngImagePlugin.PngInfo()
for key, value in drm_metadata.items():
    info.add_text(key, value)
image.save('./tmp/gradient_tile_colorimetry_drm.png', "PNG", pnginfo=info)

print("TIFF image with tiling and placeholder for Colorimetry Tags saved to ./tmp/gradient_tile_colorimetry.tiff")
print("Thumbnail subfile saved to ./tmp/gradient_tile_colorimetry_thumbnail.tiff")
print("Demo PNG with DRM metadata saved to ./tmp/gradient_tile_colorimetry_drm.png")
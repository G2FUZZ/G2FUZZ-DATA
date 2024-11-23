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
drm_metadata = {
    "Copyright": "Copyright 2023, The Image Creator",
    "Usage Rights": "No reproduction or distribution without permission."
}

# Saving a version with "DRM" metadata (demonstration with PNG, as an example)
info = PngImagePlugin.PngInfo()
for key, value in drm_metadata.items():
    info.add_text(key, value)
image.save('./tmp/gradient_tile_colorimetry_drm.png', "PNG", pnginfo=info)

# JPEG-in-TIFF feature
# Convert the image to JPEG and then save it as a JPEG-in-TIFF
# This approach saves the image in JPEG format within a TIFF container
jpeg_in_tiff_path = './tmp/gradient_tile_colorimetry_jpeg_in_tiff.tiff'
# First, save the image as a JPEG
jpeg_temp_path = './tmp/gradient_temporary.jpeg'
image.save(jpeg_temp_path, format='JPEG')
# Then, open the JPEG image and save it as TIFF
with Image.open(jpeg_temp_path) as jpeg_image:
    jpeg_image.save(jpeg_in_tiff_path, format='TIFF')

# Cleanup: Remove the temporary JPEG file
os.remove(jpeg_temp_path)

print("TIFF image with tiling and placeholder for Colorimetry Tags saved to ./tmp/gradient_tile_colorimetry.tiff")
print("Thumbnail subfile saved to ./tmp/gradient_tile_colorimetry_thumbnail.tiff")
print("Demo PNG with DRM metadata saved to ./tmp/gradient_tile_colorimetry_drm.png")
print("JPEG-in-TIFF image saved to ./tmp/gradient_tile_colorimetry_jpeg_in_tiff.tiff")
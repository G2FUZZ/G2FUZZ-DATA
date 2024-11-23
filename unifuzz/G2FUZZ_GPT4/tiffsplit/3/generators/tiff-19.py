from PIL import Image
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
# For the subfiles feature, we'll create a thumbnail of the main image
thumbnail_size = (64, 64)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the main image with tiling
image.save('./tmp/gradient_tile_colorimetry.tiff', format='TIFF', tile=('tile', 128, 128))

# The Subfiles (thumbnails or reduced-resolution images) could be saved separately
# since the standard PIL library does not directly support embedding them within the same file.
# For demonstration purposes, the thumbnail will be saved as a separate file.
# In a real application, additional steps might be necessary to embed the thumbnail as a subfile within the TIFF according to TIFF specifications.
thumbnail.save('./tmp/gradient_tile_colorimetry_thumbnail.tiff', format='TIFF')

print("TIFF image with tiling and placeholder for Colorimetry Tags saved to ./tmp/gradient_tile_colorimetry.tiff")
print("Thumbnail subfile saved to ./tmp/gradient_tile_colorimetry_thumbnail.tiff")
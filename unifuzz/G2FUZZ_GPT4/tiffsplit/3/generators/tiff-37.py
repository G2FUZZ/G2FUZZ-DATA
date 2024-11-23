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
thumbnail_size = (64, 64)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the main image with tiling
image.save('./tmp/gradient_tile_colorimetry_with_private_tag.tiff', format='TIFF', tile=('tile', 128, 128))

# As before, save the thumbnail as a separate file
thumbnail.save('./tmp/gradient_tile_colorimetry_thumbnail.tiff', format='TIFF')

print("TIFF image with tiling saved to ./tmp/gradient_tile_colorimetry_with_private_tag.tiff")
print("Thumbnail subfile saved to ./tmp/gradient_tile_colorimetry_thumbnail.tiff")
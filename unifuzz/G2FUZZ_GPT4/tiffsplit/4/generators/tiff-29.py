from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")

# Convert the image to YCbCr mode for subsampling
ycbcr_image = image.convert("YCbCr")

# Save the image as a TIFF with tiles and subsampling
tile_width, tile_height = 256, 256
ycbcr_image.save('./tmp/tiled_and_subsampled_image.tiff', format='TIFF', save_all=True,
                 tile=('raw', (tile_width, tile_height)), subsampling='4:2:0')

print("TIFF image with tiles and subsampling saved successfully.")
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")

# Save the image as a TIFF with tiles
tile_width, tile_height = 256, 256
image.save('./tmp/tiled_image.tiff', format='TIFF', tile=('raw', (tile_width, tile_height)))

print("TIFF image with tiles saved successfully.")
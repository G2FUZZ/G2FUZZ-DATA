from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image with multiple layers and custom tags
image = Image.new('RGBA', (400, 400))  # RGBA mode for alpha channel
layer1 = Image.new('RGBA', (400, 400), color=(255, 0, 0, 128))  # Red semi-transparent layer
layer2 = Image.new('RGBA', (400, 400), color=(0, 255, 0, 128))  # Green semi-transparent layer

# Define additional file features
resolution = (300, 300)  # Set resolution to 300 dpi
metadata = {'author': 'Jane Smith', 'description': 'Custom tags and multiple layers for testing'}  # Add metadata information
tile_size = (128, 128)  # Set tile size for tiled organization

# Save the image with additional file features, custom tags, multiple layers, and tiled organization
with TiffWriter('./tmp/complex_tiff_file_complex.tiff') as tif:
    tif.save(image, metadata=metadata, tile=tile_size, resolution=resolution)  # Tiled organization and additional file features
    tif.save(layer1, tile=tile_size)
    tif.save(layer2, tile=tile_size)
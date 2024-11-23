from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image with multiple layers and custom tags
image = Image.new('RGBA', (400, 400))  # RGBA mode for alpha channel
layer1 = Image.new('RGBA', (400, 400), color=(255, 0, 0, 128))  # Red semi-transparent layer
layer2 = Image.new('RGBA', (400, 400), color=(0, 255, 0, 128))  # Green semi-transparent layer

# Define custom tags for each layer
custom_tags_image = {
    'Layer': '0', 'Description': 'Base Image'
}
custom_tags_layer1 = {
    'Layer': '1', 'Description': 'Red Semi-Transparent Layer'
}
custom_tags_layer2 = {
    'Layer': '2', 'Description': 'Green Semi-Transparent Layer'
}

# Save the image with custom tags, multiple layers, and tiled organization
with TiffWriter('./tmp/complex_tiff_file_mutated.tiff') as tif:
    tif.save(image, metadata=custom_tags_image, tile=(128, 128))  # Tiled organization
    tif.save(layer1, metadata=custom_tags_layer1, tile=(128, 128))
    tif.save(layer2, metadata=custom_tags_layer2, tile=(128, 128))
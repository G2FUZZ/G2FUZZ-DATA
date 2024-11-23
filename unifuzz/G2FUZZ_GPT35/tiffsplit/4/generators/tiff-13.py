from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image
image = Image.new('RGBA', (100, 100))  # RGBA mode for alpha channel

# Add metadata information
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'Creation Date': '2022-09-15',
    'Compression Options': 'CCITT Group 4',
    'Layers and Alpha Channels': 'Supports layers for image editing and alpha channels for transparency effects'
}

# Save the image with metadata
with TiffWriter('./tmp/metadata_example_with_layers.tiff') as tif:
    tif.save(image, metadata=metadata)
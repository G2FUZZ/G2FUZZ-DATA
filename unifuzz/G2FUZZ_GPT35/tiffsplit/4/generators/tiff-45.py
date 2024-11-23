from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image with multiple layers
image1 = Image.new('RGB', (100, 100), color='red')
image2 = Image.new('RGB', (100, 100), color='green')
image3 = Image.new('RGB', (100, 100), color='blue')

# Add metadata information for each layer
metadata1 = {'Layer': '1', 'Description': 'Red Layer'}
metadata2 = {'Layer': '2', 'Description': 'Green Layer'}
metadata3 = {'Layer': '3', 'Description': 'Blue Layer'}

# Save the images with metadata as layers in a single TIFF file
with TiffWriter('./tmp/multi_layer_tiff.tiff') as tif:
    tif.save(image1, metadata=metadata1)
    tif.save(image2, metadata=metadata2)
    tif.save(image3, metadata=metadata3)

# Set custom resolution information
resolution_metadata = {
    'XResolution': (300, 1),
    'YResolution': (300, 1),
    'ResolutionUnit': 2  # inches
}

# Save the image with custom resolution metadata
with TiffWriter('./tmp/custom_resolution_tiff.tiff') as tif:
    tif.save(image1, resolution=(300.0, 300.0), metadata=resolution_metadata)
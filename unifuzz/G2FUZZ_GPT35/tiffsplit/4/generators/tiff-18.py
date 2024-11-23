from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image
image = Image.new('RGB', (100, 100))

# Add metadata information
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'Creation Date': '2022-09-15',
    'Compression Options': 'CCITT Group 4',
    'Image Masks': 'TIFF files can contain image masks for defining areas of opacity or transparency.'
}

# Save the image with metadata
with TiffWriter('./tmp/metadata_example_with_masks.tiff') as tif:
    tif.save(image, metadata=metadata)
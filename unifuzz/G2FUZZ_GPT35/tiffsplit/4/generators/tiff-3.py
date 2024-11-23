from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image
image = Image.new('RGB', (100, 100))

# Add metadata information
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'Creation Date': '2022-09-15'
}

# Save the image with metadata
with TiffWriter('./tmp/metadata_example.tiff') as tif:
    tif.save(image, metadata=metadata)
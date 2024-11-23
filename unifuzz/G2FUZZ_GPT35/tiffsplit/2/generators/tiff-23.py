from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF file with metadata and thumbnail image
metadata = {
    'Author': 'John Doe',
    'CreationDate': '2021-09-15',
    'Keywords': ['nature', 'landscape', 'mountain']
}

img_data = Image.new('RGB', (100, 100), color='red')
thumbnail_data = Image.new('RGB', (50, 50), color='green')

with TiffWriter('./tmp/metadata_thumbnail_example.tiff') as tiff:
    tiff.save(img_data, metadata=metadata)
    tiff.save(thumbnail_data, compression=None) # Save thumbnail image without compression
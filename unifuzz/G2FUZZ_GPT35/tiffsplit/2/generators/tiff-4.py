from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF file with metadata
metadata = {
    'Author': 'John Doe',
    'CreationDate': '2021-09-15',
    'Keywords': ['nature', 'landscape', 'mountain']
}

img_data = Image.new('RGB', (100, 100), color='red')

with TiffWriter('./tmp/metadata_example.tiff') as tiff:
    tiff.save(img_data, metadata=metadata)
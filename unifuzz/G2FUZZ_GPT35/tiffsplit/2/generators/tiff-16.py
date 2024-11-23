from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF file with metadata, Image Editing Capabilities, and Exif Data
metadata = {
    'Author': 'John Doe',
    'CreationDate': '2021-09-15',
    'Keywords': ['nature', 'landscape', 'mountain'],
    'Image Editing Capabilities': 'TIFF files support layers, masks, and other editing features that make them suitable for professional image editing workflows.',
    'Exif Data': 'TIFF files can store Exif (Exchangeable Image File Format) data, including information about the camera settings and conditions when the image was captured.'
}

img_data = Image.new('RGB', (100, 100), color='red')

with TiffWriter('./tmp/metadata_example_with_capabilities_and_exif.tiff') as tiff:
    tiff.save(img_data, metadata=metadata)
from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF file with metadata and Image Editing Capabilities
metadata = {
    'Author': 'John Doe',
    'CreationDate': '2021-09-15',
    'Keywords': ['nature', 'landscape', 'mountain'],
    'Image Editing Capabilities': 'TIFF files support layers, masks, and other editing features that make them suitable for professional image editing workflows.',
    'Digital Signatures': 'TIFF files can be digitally signed to verify the authenticity and integrity of the image data.',
    'Color Profiles': 'TIFF files can embed color profiles to ensure consistent color reproduction across different devices and applications.'
}

img_data = Image.new('RGB', (100, 100), color='red')

with TiffWriter('./tmp/metadata_example_with_capabilities_and_digital_signatures_and_color_profiles.tiff') as tiff:
    tiff.save(img_data, metadata=metadata)
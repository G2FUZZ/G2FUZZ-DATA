from PIL import Image
from tifffile import TiffWriter

# Create a new TIFF image
image = Image.new('RGB', (100, 100))

# Add metadata information
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'Creation Date': '2022-09-15',
    'Exif Data': {
        'Exposure Time': '1/60',
        'F-Number': 'f/2.8',
        'ISO Speed Ratings': 100,
        'Exposure Bias Value': '0',
        'Focal Length': '50mm',
        'Lens Model': 'Canon EF 50mm f/1.8 STM'
    }
}

# Save the image with metadata
with TiffWriter('./tmp/metadata_example_with_exif.tiff') as tif:
    tif.save(image, metadata=metadata)
import os
from PIL import Image

# Create a directory to save generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Create a sample image
image = Image.new('RGB', (100, 100), color='red')

# Add metadata to the image
metadata = {
    'EXIF': {
        'Make': 'Python Imaging Library',
        'Model': '1.0',
        'Software': 'PIL',
        'DateTime': '2022-01-01 12:00:00',
        'ExposureTime': '1/100',
        'FNumber': 'f/2.8',
        'ISO': 100
    }
}
image.info['jfif'] = metadata

# Save the image with metadata as a jpg file
image.save('./tmp/metadata_example.jpg', format='JPEG')

print('Metadata added to the jpg file successfully.')
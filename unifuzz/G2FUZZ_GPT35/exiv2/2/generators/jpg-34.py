import os
from PIL import Image

# Create a sample image
image = Image.new('RGB', (200, 200), color='blue')

# Add metadata to the image
metadata = {
    'EXIF': {
        'DateTime': '2022-01-01 12:00:00',
        'CameraModel': 'Nikon D850',
        'Location': 'Paris'
    },
    'GPSInfo': {
        'GPSLatitude': '48.8566 N',
        'GPSLongitude': '2.3522 E'
    },
    'IPTC': {
        'Byline': 'John Doe',
        'Caption': 'Eiffel Tower at sunset'
    }
}
image.info['jfif'] = metadata

# Save the image with metadata
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')
image.save('./tmp/complex_image.jpg')

print("Complex image with metadata saved successfully.")
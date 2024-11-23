import os
from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='blue')

# Add metadata to the image
metadata = {
    'EXIF': {
        'DateTime': '2022-01-01 12:00:00',
        'CameraModel': 'Canon EOS 5D Mark IV',
        'Location': 'New York City'
    },
    'ColorProfiles': {
        'ProfileName': 'sRGB',
        'ProfileVersion': '2.1'
    }
}
image.info['jfif'] = metadata

# Save the image with metadata and as Progressive JPEG
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')
image.save('./tmp/sample_with_color_profiles.jpg', format='JPEG', progressive=True)

print("Image with metadata, Color profiles, and Progressive JPEG feature saved successfully.")
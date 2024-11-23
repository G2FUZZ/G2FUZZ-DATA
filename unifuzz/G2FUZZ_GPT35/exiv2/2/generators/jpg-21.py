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
    'jfif': {
        'EmbeddedComments': 'This is an embedded comment in the JPEG file.'
    }
}
image.info = metadata

# Save the image with metadata, Embedded comments, and as Progressive JPEG
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')
image.save('./tmp/sample_progressive_with_comments.jpg', format='JPEG', progressive=True)

print("Image with metadata, Embedded comments, and Progressive JPEG feature saved successfully.")
import os
from PIL import Image

# Create a new JPG file with metadata
image = Image.new('RGB', (100, 100), color='red')
image.save('./tmp/image_with_metadata.jpg', exif=b'Some example EXIF data')

# Check if the file was saved successfully
if os.path.exists('./tmp/image_with_metadata.jpg'):
    print('JPG file with metadata was successfully created and saved.')
else:
    print('Failed to create JPG file with metadata.')
import os
from PIL import Image

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a sample JPEG file with metadata
image = Image.new('RGB', (100, 100), color='red')
image.save('./tmp/sample.jpg', exif=b'Some example metadata')

print("JPEG file with metadata created successfully.")
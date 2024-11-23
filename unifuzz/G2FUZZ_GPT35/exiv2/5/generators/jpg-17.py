import os
from PIL import Image

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a sample JPEG file with metadata and image editing compatibility
image = Image.new('RGB', (100, 100), color='red')
image.save('./tmp/sample_with_editing_compatibility.jpg', exif=b'Some example metadata', quality=95)

print("JPEG file with metadata and image editing compatibility created successfully.")
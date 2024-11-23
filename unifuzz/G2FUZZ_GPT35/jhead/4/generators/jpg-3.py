import os
from PIL import Image
from PIL.ExifTags import TAGS
import json

# Create a directory to store the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample image with metadata (EXIF data)
image = Image.new('RGB', (100, 100), color='red')
exif_data = {
    271: 'Canon',
    272: 'Canon EOS 5D Mark IV',
    274: 1,
    306: '2022:10:01 15:30:00',
    36867: '2022:10:01 15:30:00',
}

# Convert the exif_data dictionary to bytes
exif_bytes = {TAGS[key]: exif_data[key] for key in exif_data}
exif_bytes_json = json.dumps(exif_bytes).encode('utf-8')
image.save('./tmp/sample_image.jpg', exif=exif_bytes_json)
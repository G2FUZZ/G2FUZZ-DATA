import os
from PIL import Image
from PIL.ExifTags import TAGS

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Create a blank image to represent a jpg file with metadata
img = Image.new('RGB', (100, 100), color='white')

# Add EXIF data (example data)
exif_data = {
    TAGS[key]: value for key, value in {
        271: 'Canon',
        272: 'Canon EOS 5D Mark IV',
        306: '2022:08:15 10:30:00',
        36867: '2022:08:15 10:30:00',
    }.items()
}

# Convert the EXIF data dictionary to bytes
exif_bytes = img.info['exif'] if 'exif' in img.info else b''
for tag, value in exif_data.items():
    tag_id = TAGS.get(tag)
    if tag_id:
        exif_bytes += tag_id + b'\x00' + value.encode() + b'\x00'

# Save the image with EXIF data
img.save('./tmp/example.jpg', exif=exif_bytes)

print("Generated jpg file with metadata successfully.")
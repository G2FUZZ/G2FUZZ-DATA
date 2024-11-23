from PIL import Image, ExifTags
from datetime import datetime
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image
img = Image.new('RGB', (100, 100), color=(73, 109, 137))

# Add EXIF data
exif_data = img.getexif()

# Find the key for 'DateTime', 'Make', and 'Model' in ExifTags.TAGS
date_time_key = None
make_key = None
model_key = None
for key, value in ExifTags.TAGS.items():
    if value == 'DateTime':
        date_time_key = key
    elif value == 'Make':
        make_key = key
    elif value == 'Model':
        model_key = key

# Assuming the keys were found, update the EXIF data
if date_time_key is not None:
    exif_data[date_time_key] = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
if make_key is not None:
    exif_data[make_key] = 'Python PIL'
if model_key is not None:
    exif_data[model_key] = 'Generated Image'

# Convert the updated EXIF data to binary
exif_bytes = exif_data.tobytes()

# Save the image with EXIF data
file_path = './tmp/image_with_exif.jpg'
img.save(file_path, 'JPEG', exif=exif_bytes)

print(f'Image with EXIF data saved to {file_path}')
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import io

# Create a new image with a gradient background
img = Image.new('RGB', (400, 400))

for y in range(img.height):
    for x in range(img.width):
        img.putpixel((x, y), (x, y, 255))

# Add EXIF data to the image
exif_data = {
    TAGS.get(key, key): str(value).encode('utf-8')
    for key, value in {
        271: 'Sample Software',
        272: 'Sample Camera Model',
        306: '2022:01:01 12:00:00',  # Date and time (YYYY:MM:DD HH:MM:SS)
        33434: (1, 100),  # Exposure time
        33437: (22, 10),  # F-stop
        34850: (200, 1),  # ISO speed
    }.items()
}

# Convert exif_data to bytes
exif_bytes = io.BytesIO()
for key, value in exif_data.items():
    exif_bytes.write(key.encode('utf-8'))
    exif_bytes.write(b'\x00')
    exif_bytes.write(value)
exif_bytes = exif_bytes.getvalue()

img.save('./tmp/complex_image.jpg', format='JPEG', quality=95, exif=exif_bytes)
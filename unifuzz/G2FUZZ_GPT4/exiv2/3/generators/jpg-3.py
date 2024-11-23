from PIL import Image
import piexif
from datetime import datetime
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument name here

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'blue')

# Prepare Exif data (using piexif)
exif_ifd = {
    piexif.ExifIFD.CameraOwnerName: u"John Doe",
    piexif.ExifIFD.DateTimeOriginal: datetime.now().strftime('%Y:%m:%d %H:%M:%S'),
    piexif.ExifIFD.LensMake: u"Sample Lens",
}

exif_dict = {"Exif": exif_ifd}
exif_bytes = piexif.dump(exif_dict)

# Save the image with Exif data
img.save('./tmp/sample_image_with_exif.jpg', exif=exif_bytes)

print("Image with Exif data saved.")
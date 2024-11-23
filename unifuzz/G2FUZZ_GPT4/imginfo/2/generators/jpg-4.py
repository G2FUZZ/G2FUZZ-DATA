from PIL import Image
import os
import io
import piexif
from piexif import GPSIFD

# Create a directory for storing the output if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color=(73, 109, 137))

# Prepare Exif data
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: u"FakeMake",
        piexif.ImageIFD.Model: "FakeCameraModel",
        piexif.ImageIFD.Software: "FakeSoftware",
        piexif.ImageIFD.DateTime: "2023:09:28 10:00:00",
    },
    "Exif": {},
    "GPS": {
        GPSIFD.GPSLatitudeRef: 'N',
        GPSIFD.GPSLatitude: ((40, 1), (42, 1), (0, 1)),
        GPSIFD.GPSLongitudeRef: 'W',
        GPSIFD.GPSLongitude: ((74, 1), (0, 1), (0, 1)),
    }
}

# Convert the Exif data to bytes
exif_bytes = piexif.dump(exif_dict)

# Add the Exif data to the image
img.save(os.path.join(output_dir, 'image_with_exif.jpg'), 'JPEG', exif=exif_bytes)

print('Image with Exif data saved.')
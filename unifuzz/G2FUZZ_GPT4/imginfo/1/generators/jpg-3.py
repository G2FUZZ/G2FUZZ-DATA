import os
from PIL import Image
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Define some Exif data
# Note: GPS and other data should be in specific formats as per Exif specification
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: u"Canon",
        piexif.ImageIFD.XResolution: (96, 1),
        piexif.ImageIFD.YResolution: (96, 1),
        piexif.ImageIFD.Software: u"piexif"
    },
    "Exif": {
        piexif.ExifIFD.DateTimeOriginal: u"2023:01:01 10:00:00",
        piexif.ExifIFD.LensMake: u"Canon",
        piexif.ExifIFD.Sharpness: 65535,
        piexif.ExifIFD.LensSpecification: ((24, 1), (105, 1), (4, 1), (4, 1)),
    },
    "GPS": {
        piexif.GPSIFD.GPSLatitudeRef: u"N",
        piexif.GPSIFD.GPSLatitude: ((34, 1), (56, 1), (0, 1)),
        piexif.GPSIFD.GPSLongitudeRef: u"W",
        piexif.GPSIFD.GPSLongitude: ((118, 1), (24, 1), (0, 1)),
    }
}

# Convert Exif data to bytes
exif_bytes = piexif.dump(exif_dict)

# Save the image with Exif data
img.save('./tmp/test_image_with_exif.jpg', exif=exif_bytes)

print("Image with Exif data saved to ./tmp/test_image_with_exif.jpg")
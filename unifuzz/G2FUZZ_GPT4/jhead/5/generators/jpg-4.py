import os
from PIL import Image, ExifTags
from datetime import datetime
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Prepare EXIF data
# Note: The ExifTags module provides a TAGS dictionary that maps exif tag numbers to tag names.
# However, for setting Exif data, we need to use the specific codes in their raw form.
# piexif uses a different structure to hold Exif information, which is a dictionary where each key represents an IFD
# (Image File Directory - such as "0th", "Exif", "GPS", and "1st").
exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

# Convert datetime format to EXIF date format
dt_original = datetime.now().strftime("%Y:%m:%d %H:%M:%S")

# Using piexif.ExifIFD.DateTimeOriginal as the key to store the original date/time of the photo
exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = dt_original

# GPS Data (Example: Lat 25.0329636, Long 121.5654268)
# Note: GPS latitude and longitude values must be in the (degrees, minutes, seconds) format, each part represented as a rational (numerator, denominator).
exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "N"
exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = [(25, 1), (1, 1), (5957, 100)]
exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = "E"
exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = [(121, 1), (33, 1), (2563, 100)]

# Dump exif_dict to bytes
exif_bytes = piexif.dump(exif_dict)

# Save the image with EXIF data
img.save('./tmp/with_exif.jpg', 'JPEG', exif=exif_bytes)

print("Image with EXIF data saved to './tmp/with_exif.jpg'")
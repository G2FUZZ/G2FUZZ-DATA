from PIL import Image, ExifTags
import os
import io
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Prepare EXIF data
exif_dict = {
    "0th": {},
    "Exif": {},
    "GPS": {},
    "1st": {},
    "thumbnail": None
}

# Mapping ExifTags.TAGS to their corresponding piexif tags
for tag, value in ExifTags.TAGS.items():
    if value == "DateTime":
        exif_dict["0th"][piexif.ImageIFD.DateTime] = '2023:01:01 00:00:00'
    elif value == "Make":
        exif_dict["0th"][piexif.ImageIFD.Make] = 'MyCameraBrand'
    elif value == "Model":
        exif_dict["0th"][piexif.ImageIFD.Model] = 'MyCameraModel'

# Manually setting GPSInfo since we know the structure
exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = 'N'
exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = [(40, 1), (26, 1), (0, 1)]
exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = 'W'
exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = [(74, 1), (0, 1), (0, 1)]

# Convert our dictionary to bytes
exif_bytes = piexif.dump(exif_dict)

# Save the image with EXIF data
img.save('./tmp/sample_with_exif.jpg', exif=exif_bytes)

# To add Restart Markers, we need to manipulate the JPEG directly since PIL doesn't support this natively.
# We will convert the image to JPEG format in memory, then add restart markers manually.
# This process is somewhat more involved and requires understanding of JPEG format and markers.

# Save image to bytes buffer
buffer = io.BytesIO()
img.save(buffer, format='JPEG')

# JPEG uses 0xFFD0 to 0xFFD7 for restart markers, let's add one example
jpeg_data = buffer.getvalue()
# Finding the end of the JPEG header (0xFFDA marker)
header_end = jpeg_data.find(b'\xFF\xDA') + 2

# Insert a restart marker (0xFFD0) after the header
jpeg_with_restart = jpeg_data[:header_end] + b'\xFF\xD0' + jpeg_data[header_end:]

# Save the modified image data with a restart marker
with open('./tmp/sample_with_restart_marker.jpg', 'wb') as f:
    f.write(jpeg_with_restart)

print("Image with Restart Markers saved.")
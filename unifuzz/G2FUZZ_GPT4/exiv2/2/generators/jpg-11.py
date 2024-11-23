from PIL import Image, ExifTags
import os
import io
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color = 'red')

# Prepare EXIF data
# Note: The EXIF tags are not very human-friendly, so we use ExifTags for reverse mapping
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
# The "Quantization" process is an inherent part of the JPEG compression method and not directly
# controlled through the PIL or piexif interfaces. However, you can control the quality parameter,
# which indirectly affects the quantization process.
quality_level = 85  # Lower numbers increase compression and reduce quality, thereby affecting quantization.
img.save('./tmp/sample_with_exif_and_quantization.jpg', 'JPEG', exif=exif_bytes, quality=quality_level)

print("Image with EXIF data and quantization saved.")
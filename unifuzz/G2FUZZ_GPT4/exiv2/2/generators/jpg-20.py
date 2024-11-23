from PIL import Image, ExifTags
import os
import io
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color='red')

# Create different resolutions for hierarchical storage
sizes = [(100, 100), (50, 50), (25, 25)]  # Example sizes for demonstration
images = [img.resize(size) for size in sizes]

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

# Manually setting GPSInfo
exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = 'N'
exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = [(40, 1), (26, 1), (0, 1)]
exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = 'W'
exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = [(74, 1), (0, 1), (0, 1)]

# Convert our dictionary to bytes
exif_bytes = piexif.dump(exif_dict)

# Save the main image with EXIF data
quality_level = 85
img.save('./tmp/sample_with_exif_and_quantization.jpg', 'JPEG', exif=exif_bytes, quality=quality_level)

# Saving hierarchical images in the same directory with different names
for idx, image in enumerate(images):
    image.save(f'./tmp/sample_hierarchical_{idx}.jpg', 'JPEG', quality=quality_level)

# MPF (Multi-Picture Format) addition starts here
# Prepare MPF data
mpf_dict = {
    "MPFVersion": (0, 1, 0, 0),
    "NumberOfImages": len(images),
    "MPEntry": [],
}

# Placeholder for individual image offsets and sizes, to be updated later
offset = 0
for i, image in enumerate(images):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_size = img_byte_arr.tell()
    mpf_dict["MPEntry"].append({
        "IndividualImageUID": i + 1,
        "IndividualImageDataOffset": offset,
        "IndividualImageSize": img_size,
        # Other necessary fields can be added here
    })
    offset += img_size

# Since MPF is not directly supported by piexif or PIL, we need a custom method to append MPF data.
# This is a placeholder to illustrate the concept. Actual implementation requires writing MPF data
# to the JPEG file according to the MPF specification, which is beyond simple script capabilities
# without an existing library that supports MPF.

print("Main image, hierarchical images, and MPF data prepared (MPF data needs custom implementation to append to JPEG).")
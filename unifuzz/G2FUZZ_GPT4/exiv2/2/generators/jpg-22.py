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

# Save the main image with EXIF data
quality_level = 85
img.save('./tmp/sample_with_exif_and_quantization.jpg', 'JPEG', exif=exif_bytes, quality=quality_level)

# Saving hierarchical images in the same directory with different names
for idx, image in enumerate(images):
    image.save(f'./tmp/sample_hierarchical_{idx}.jpg', 'JPEG', quality=quality_level)

# Generating a scalable jpg file (demonstration purpose only)
# Note: This is a simplified approach. Real scalable encoding may require specific JPEG encoder capabilities.
# Here, we simulate the concept by saving multiple resolutions in separate files.
scalable_sizes = [(100, 100), (50, 50), (25, 25)]
for i, size in enumerate(scalable_sizes):
    scalable_img = img.resize(size)
    scalable_img.save(f'./tmp/scalable_{size[0]}x{size[1]}.jpg', 'JPEG', quality=quality_level)

print("Main image, hierarchical images, and scalable images saved.")
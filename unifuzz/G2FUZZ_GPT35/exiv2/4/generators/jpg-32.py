from PIL import Image
from PIL import JpegImagePlugin
from PIL.ExifTags import TAGS
from io import BytesIO

# Create a new RGB image
image = Image.new('RGB', (200, 200))

# Add custom quantization tables to the image
quantization = [
    [10, 8, 6, 10, 16, 26, 36, 46],
    [8, 8, 10, 14, 20, 46, 48, 44],
    [10, 9, 12, 20, 36, 45, 57, 44],
    [10, 13, 18, 25, 46, 82, 75, 57],
    [14, 18, 33, 52, 64, 105, 99, 73],
    [20, 31, 51, 60, 77, 100, 109, 88],
    [45, 60, 74, 83, 99, 117, 116, 97],
    [68, 88, 91, 94, 108, 96, 99, 95]
]

JpegImagePlugin.DQT = quantization

# Set author information in metadata
metadata = {
    TAGS.get(315): 'John Doe',  # Author information tag
    TAGS.get(306): 'Adobe Photoshop'  # Software used to create the image tag
}

# Convert metadata to bytes-like object
metadata_bytes = bytes(str(metadata), 'utf-8')

image.save('./tmp/rgb_image_with_custom_features.jpg', quality=95, optimize=True, progressive=True, exif=metadata_bytes)
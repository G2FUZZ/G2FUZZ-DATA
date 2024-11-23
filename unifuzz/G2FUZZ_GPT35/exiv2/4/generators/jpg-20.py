from PIL import Image
from PIL.ExifTags import TAGS

# Create a new image
image = Image.new('RGB', (100, 100), color='red')

# Get valid Exif tags
valid_tags = {k: v for k, v in TAGS.items() if isinstance(k, int)}

# Add metadata (Exif data)
exif_data = {
    valid_tags[key]: f"Value_{key}" for key in range(10) if key in valid_tags
}

# Additional features
exif_data['Lossless transformations'] = "Supports rotation and cropping without quality loss."
exif_data['Huffman coding'] = "Uses Huffman coding to compress image data."

# Convert exif_data to bytes
exif_bytes = bytes(str(exif_data), 'utf-8')

image.save('./tmp/test.jpg', exif=exif_bytes)
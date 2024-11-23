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

# Add Chroma subsampling feature
exif_data['ChromaSubsampling'] = '4:2:0'  # Example value for Chroma subsampling

# Add Embedded color profiles feature
exif_data['ColorSpace'] = 'sRGB'  # Example value for Embedded color profiles (sRGB)

# Convert exif_data to bytes
exif_bytes = bytes(str(exif_data), 'utf-8')

image.save('./tmp/test_with_color_profiles.jpg', exif=exif_bytes)
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

# Convert exif_data to bytes
exif_bytes = bytes(str(exif_data), 'utf-8')

# Add comment marker
comment_marker = b'Comment markers: JPG files can include comment markers to store textual information or metadata within the file.'

# Save image with Exif data and comment marker
image.save('./tmp/test_with_comment.jpg', exif=exif_bytes, icc_profile=comment_marker)
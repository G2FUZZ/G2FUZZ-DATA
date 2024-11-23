from PIL import Image
import json

# Create a white image
white_image = Image.new('RGB', (100, 100), 'white')

# Add metadata to the image
metadata = {
    'Copyright': 'Copyright 2021',
    'Author': 'John Doe',
    'Keywords': ['white', 'image', 'metadata']
}

# Serialize metadata to JSON and encode to bytes
exif_bytes = json.dumps(metadata).encode('utf-8')

# Save the image with metadata
file_path = './tmp/white_image_with_metadata.jpg'
white_image.save(file_path, quality=100, icc_profile=b'', exif=exif_bytes)

print('Image with metadata saved successfully.')
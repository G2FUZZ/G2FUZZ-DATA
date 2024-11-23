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

# Add ICC Profiles to the metadata
icc_profiles = {
    'ProfileName': 'sRGB',
    'Version': '2.1.0',
    'Class': 'Display Device Profile',
    'ColorSpace': 'RGB'
}
metadata['ICC Profiles'] = icc_profiles

# Serialize metadata to JSON and encode to bytes
exif_bytes = json.dumps(metadata).encode('utf-8')

# Save the image with metadata and ICC Profiles
file_path = './tmp/white_image_with_metadata_and_icc.jpg'
white_image.save(file_path, quality=100, icc_profile=b'IHDR\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', exif=exif_bytes)

print('Image with metadata and ICC Profiles saved successfully.')
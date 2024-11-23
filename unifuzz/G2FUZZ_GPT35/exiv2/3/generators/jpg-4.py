import os
from PIL import Image

# Create a new image
img = Image.new('RGB', (100, 100), color='white')

# Add metadata to the image
metadata = {
    'Exif': {
        271: 'Camera Model Name',
        272: 'Image Description',
        274: 'Orientation',
        306: 'DateTime',
        531: 'YCbCr Positioning'
    }
}
img.info['jfif'] = metadata

# Save the image with metadata
output_path = './tmp/metadata_example.jpg'
img.save(output_path)

print(f"Image with metadata saved at {output_path}")
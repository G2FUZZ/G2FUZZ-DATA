import os
from PIL import Image

# Create a sample image
image = Image.new('RGB', (100, 100), color='red')

# Add metadata to the image
metadata = {
    'exif': {
        271: 'Camera Model',  # Camera Make
        272: 'Camera Model',  # Camera Model
        306: '2021:09:03 10:00:00',  # Date and Time
    }
}
image.info['exif'] = metadata['exif']

# Save the image with metadata
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)
image.save(os.path.join(output_dir, 'sample.jpg'))

print('Image with metadata saved successfully.')
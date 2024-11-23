import os
from PIL import Image

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample image
image = Image.new('RGB', (100, 100), color = 'red')
image.save('./tmp/sample.jpg')

# Add metadata to the image
image = Image.open('./tmp/sample.jpg')
metadata = {
    'Title': 'Sample Image',
    'Author': 'John Doe',
    'Date': '2022-01-01'
}
image.info['metadata'] = metadata
image.save('./tmp/sample_with_metadata.jpg')
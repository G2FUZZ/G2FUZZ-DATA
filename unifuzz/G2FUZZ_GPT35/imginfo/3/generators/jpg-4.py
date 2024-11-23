from PIL import Image

# Create a new image
image = Image.new('RGB', (100, 100))

# Adding metadata to the image
metadata = {
    'Camera Model': 'Canon EOS 5D Mark IV',
    'Date Taken': '2022-01-01',
    'Exposure Time': '1/100 sec',
    'Aperture': 'f/2.8',
    'ISO': 200
}

image.info['metadata'] = metadata

# Save the image with metadata
image.save('./tmp/metadata_example.jpg')
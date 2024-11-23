import os
from PIL import Image
from PIL.ExifTags import TAGS

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample image
image = Image.new('RGB', (200, 200), color='blue')
image.save('./tmp/sample_complex.jpg')

# Add metadata and EXIF data to the image
image = Image.open('./tmp/sample_complex.jpg')
metadata = {
    'Title': 'Complex Image',
    'Author': 'Jane Smith',
    'Date': '2022-02-15'
}
exif_data = {
    TAGS[key]: value
    for key, value in image.info.items()
    if key in TAGS
}
exif_data.update({
    'ExifVersion': '2.1',
    'Software': 'PIL',
    'DateTimeOriginal': '2022:02:15 12:00:00'
})
image.info['metadata'] = metadata
image.save('./tmp/sample_complex_with_exif.jpg')
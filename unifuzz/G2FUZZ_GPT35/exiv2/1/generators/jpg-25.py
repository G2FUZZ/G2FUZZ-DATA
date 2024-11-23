import os
from PIL import Image
from iptcinfo3 import IPTCInfo

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with metadata including 'Printability' and 'EXIF Data' features
img = Image.new('RGB', (100, 100), color='blue')
img.save('./tmp/example_with_exif_data.jpg')

# Add metadata to the jpg file
info = IPTCInfo('./tmp/example_with_exif_data.jpg', force=True)
info['keywords'] = ['example', 'metadata', 'jpg']
info['caption/abstract'] = 'JPG files can store EXIF data such as camera settings and location information.'
info.save()
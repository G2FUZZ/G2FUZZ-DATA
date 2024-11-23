import os
from PIL import Image
from iptcinfo3 import IPTCInfo

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with metadata
img = Image.new('RGB', (100, 100), color='red')
img.save('./tmp/example.jpg')

# Add metadata to the jpg file
info = IPTCInfo('./tmp/example.jpg', force=True)
info['keywords'] = ['example', 'metadata', 'jpg']
info.save()
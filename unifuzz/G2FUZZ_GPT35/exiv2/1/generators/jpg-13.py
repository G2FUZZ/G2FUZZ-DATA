import os
from PIL import Image
from iptcinfo3 import IPTCInfo

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with metadata and embedded color profiles
img = Image.new('RGB', (100, 100), color='red')
img.save('./tmp/example_with_color_profiles.jpg', icc_profile=img.info.get('icc_profile'))

# Add metadata to the jpg file
info = IPTCInfo('./tmp/example_with_color_profiles.jpg', force=True)
info['keywords'] = ['example', 'metadata', 'jpg']
info.save()
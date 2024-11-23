import os
from PIL import Image
from iptcinfo3 import IPTCInfo

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with metadata including the 'Printability' and 'Compression Levels' features
img = Image.new('RGB', (100, 100), color='blue')
img.save('./tmp/example_with_compression_levels.jpg')

# Add metadata to the jpg file
info = IPTCInfo('./tmp/example_with_compression_levels.jpg', force=True)
info['keywords'] = ['example', 'metadata', 'jpg']
info['caption/abstract'] = 'JPG files can be printed with high quality and resolution.'
info['custom1'] = 'Compression Levels: JPG files can be saved at different compression levels.'
info.save()
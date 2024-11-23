from PIL import Image, PngImagePlugin
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode and white background
image = Image.new('RGB', (640, 480), color='white')

# Prepare metadata
meta_info = PngImagePlugin.PngInfo()
meta_info.add_text('Copyright', 'Copyright 2023 by Example')
meta_info.add_text('Comment', 'Generated for demonstrating metadata storage in PNG files.')
meta_info.add_text('Creation Time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Save the image with metadata
image.save('./tmp/metadata_example.png', 'PNG', pnginfo=meta_info)

print('Image with metadata saved to ./tmp/metadata_example.png')
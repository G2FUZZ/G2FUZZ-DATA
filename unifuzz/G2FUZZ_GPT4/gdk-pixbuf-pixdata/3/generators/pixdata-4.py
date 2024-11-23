from PIL import Image, PngImagePlugin
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'blue')

# Prepare metadata
metadata = PngImagePlugin.PngInfo()
metadata.add_text('Creation Date', '2023-01-01')
metadata.add_text('Author', 'John Doe')
metadata.add_text('Copyright Notice', 'Copyright © 2023 John Doe. All rights reserved.')

# Save the image with metadata
image.save(output_dir + 'pixdata.png', 'PNG', pnginfo=metadata)
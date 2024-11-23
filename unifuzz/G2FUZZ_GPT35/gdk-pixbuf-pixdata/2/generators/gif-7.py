from PIL import Image, ImageDraw
import imageio
import os

# Create a new GIF image
gif_image = Image.new('RGB', (100, 100), color='white')

# Add metadata to the GIF image
gif_image.info['comment'] = 'This is a custom comment in the metadata'
gif_image.info['copyright'] = 'Copyright (c) 2021'

# Save the GIF image with metadata
output_folder = './tmp/'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, 'metadata.gif')
gif_image.save(output_file, save_all=True)

# Check if the file was created successfully
if os.path.exists(output_file):
    print(f'GIF file with metadata saved successfully at: {output_file}')
else:
    print('Error saving GIF file with metadata')
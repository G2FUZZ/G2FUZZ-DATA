from PIL import Image, ImageDraw, ImageFont
import imageio
import os

# Create a new GIF image
image = Image.new('RGB', (100, 100), color='white')

# Add metadata
image.info['author'] = 'John Doe'
image.info['created'] = '2022-10-15'
image.info['comments'] = 'This is a sample GIF with metadata'

# Save the image
output_path = './tmp/sample.gif'
image.save(output_path)

# Create a GIF file containing multiple frames
frames = []
for i in range(10):
    frame = Image.new('RGB', (100, 100), color='white')
    draw = ImageDraw.Draw(frame)
    font = ImageFont.load_default()
    draw.text((10, 10), f'Frame {i}', fill='black', font=font)
    frames.append(frame)

# Save the frames as a GIF
output_path_frames = './tmp/sample_frames.gif'
imageio.mimsave(output_path_frames, frames, duration=0.5)

print('GIF files with metadata and frames have been generated and saved.')
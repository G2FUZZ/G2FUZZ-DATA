import os
from PIL import Image, ImageDraw

# Create a new directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a new GIF file with a simple structure
img = Image.new('RGB', (100, 100), color='white')
frames = []

for i in range(10):
    frame = img.copy()
    draw = ImageDraw.Draw(frame)
    draw.text((10, 10), f'Frame {i}', fill='black')
    frames.append(frame)

frames[0].save('./tmp/simple_structure.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
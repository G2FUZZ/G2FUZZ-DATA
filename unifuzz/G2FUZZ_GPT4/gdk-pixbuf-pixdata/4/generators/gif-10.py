from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the properties of the GIF
width, height = 200, 200
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
frames = []

# Generate each frame
for color in colors:
    frame = Image.new('RGB', (width, height), color=color)
    frames.append(frame)

# Save the frames as a GIF
output_path = os.path.join(output_dir, 'binary_format_example.gif')
frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=400, loop=0)
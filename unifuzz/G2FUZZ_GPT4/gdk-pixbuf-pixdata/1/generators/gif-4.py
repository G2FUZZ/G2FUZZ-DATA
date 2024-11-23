from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Define the dimensions of the image
width, height = 200, 200

# Define the colors to use in the frames
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'purple']

# Generate frames
frames = []
for color in colors:
    frame = Image.new('RGB', (width, height), color=color)
    frames.append(frame)

# Save the frames as a GIF
frames[0].save('./tmp/lossless_compression_demo.gif',
               save_all=True,
               append_images=frames[1:],
               duration=300,
               loop=0,
               optimize=False)

print("GIF saved to ./tmp/lossless_compression_demo.gif")
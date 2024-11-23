import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Parameters for the GIF
width, height = 256, 256
num_frames = 10

frames = []

for i in range(num_frames):
    # Create an image with changing colors
    data = np.zeros((height, width, 3), dtype=np.uint8)
    data[:, :, 0] = i * 25  # Red channel changes
    data[:, :, 1] = 255 - i * 25  # Green channel inversely changes
    image = Image.fromarray(data, 'RGB')
    
    frames.append(image)

# Save the frames as a GIF
frames[0].save('./tmp/compression_example.gif',
               save_all=True,
               append_images=frames[1:],
               duration=100,
               loop=0,
               optimize=True)

print("GIF saved at './tmp/compression_example.gif'")
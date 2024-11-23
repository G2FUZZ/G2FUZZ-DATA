from PIL import Image
import numpy as np
import imageio

# Create a global color table with 256 colors
global_color_table = np.random.randint(0, 256, (256, 3), dtype=np.uint8)

# Convert the global color table to 'P' mode
global_color_table_image = Image.fromarray(global_color_table).convert('P')

# Create a list to store frames
frames = []

# Create 5 frames with random colors using the global color table
for _ in range(5):
    frame = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    frames.append(Image.fromarray(frame).quantize(palette=global_color_table_image))

# Save the frames as a gif file
imageio.mimsave('./tmp/global_color_table.gif', frames, duration=0.5)
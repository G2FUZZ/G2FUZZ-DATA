import imageio
import numpy as np

# Generate a sample image
width, height = 100, 100
image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Save the image as a gif with lossless compression (LZW)
imageio.mimwrite('./tmp/sample.gif', [image], format='GIF', duration=0.1, subrectangles=False, palettesize=256)
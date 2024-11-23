import numpy as np
import imageio

# Create a random image as an example
image_data = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

# Save the image as an animated GIF with compression
imageio.mimsave('./tmp/example.gif', [image_data], fps=1)
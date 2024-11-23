import imageio
import numpy as np

# Create a sample image
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :50] = [255, 0, 0]  # Left side in red
image[:, 50:] = [0, 0, 255]   # Right side in blue

# Save the image as a GIF file
imageio.mimsave('./tmp/sample.gif', [image], duration=0.5)
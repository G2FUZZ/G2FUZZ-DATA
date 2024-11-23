import numpy as np
import imageio

# Create a 100x100 transparent TGA image with alpha channel
img = np.zeros((100, 100, 4), dtype=np.uint8)
img[:, :, 0:3] = 255  # Set RGB values to white
img[:, :, 3] = 128    # Set alpha channel to 128 (transparency)

# Save the image as a TGA file
imageio.imwrite('./tmp/transparent_image.tga', img)
import numpy as np
import imageio

# Create a 100x100 image with transparency (alpha channel)
image_with_transparency = np.zeros((100, 100, 4), dtype=np.uint8)
image_with_transparency[:, :, :3] = 255  # Set RGB channels to white
image_with_transparency[:, :, 3] = 128  # Set alpha channel to 50% transparency

# Save the image as a TGA file
imageio.imwrite('./tmp/transparent_image.tga', image_with_transparency)
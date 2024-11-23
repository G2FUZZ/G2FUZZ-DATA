import imageio
import numpy as np

# Define image dimensions
width, height = 200, 200

# Create a numpy array representing a transparent image
image = np.zeros((height, width, 4), dtype=np.uint8)
image[:, :, 0] = 255  # Set red channel to maximum value
image[:, :, 3] = 0    # Set alpha channel to 0 for transparency

# Save the image as a gif file
imageio.imwrite('./tmp/transparent_image.gif', image, format='GIF', duration=0.1)
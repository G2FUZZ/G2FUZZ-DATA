import numpy as np
import imageio

# Create a sample image data
image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

# Save the image as a TIFF file
imageio.imsave('./tmp/sample_image.tiff', image_data)

print("TIFF file containing the specified feature has been generated and saved.")
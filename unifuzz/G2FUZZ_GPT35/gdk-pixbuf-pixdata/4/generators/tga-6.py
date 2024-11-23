import numpy as np

# Generate a sample image data
image_data = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

# Save the image data as a TGA file
image_data.tofile('./tmp/compressed_image.tga')
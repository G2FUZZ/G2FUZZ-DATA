import numpy as np
import imageio

# Create a list of images with metadata
images = []
for i in range(5):
    image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    image = np.full_like(image, i * 50)  # Fill with grayscale values
    image = np.concatenate((image, np.full((20, 100, 3), [255, 255, 255], dtype=np.uint8)))  # Add white metadata bar
    images.append(image)

# Save the images as a gif file
imageio.mimsave('./tmp/metadata.gif', images, duration=0.5)
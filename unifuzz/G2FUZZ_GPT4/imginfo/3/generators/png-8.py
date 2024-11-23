import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate a random noise image (representing unfiltered data)
image_height, image_width = 256, 256
noise_image = np.random.randint(0, 256, (image_height, image_width, 3), dtype=np.uint8)

# Apply a simple "filter" to the bottom half: here we'll just make it a uniform color
# to simulate making the data more homogenous and thus more compressible
noise_image[image_height//2:, :] = [128, 128, 128]

# Save the image
plt.imshow(noise_image)
plt.axis('off')  # Turn off axis numbers and ticks
plt.savefig(f'{output_dir}filtered_image.png', bbox_inches='tight', pad_inches=0)
plt.close()
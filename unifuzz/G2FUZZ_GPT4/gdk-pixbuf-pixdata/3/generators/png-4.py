import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Create an empty image with RGBA channels (Red, Green, Blue, Alpha for transparency)
# Size: 200x200 pixels
img_size = (200, 200)
img = np.zeros((*img_size, 4), dtype=np.uint8)

# Fill the image
# Red gradient horizontally
# Green constant
# Blue gradient vertically
# Alpha channel with a radial gradient for varying transparency
for y in range(img_size[1]):
    for x in range(img_size[0]):
        # Red channel - horizontal gradient
        img[y, x, 0] = (x / img_size[0]) * 255
        # Green channel - constant
        img[y, x, 1] = 128
        # Blue channel - vertical gradient
        img[y, x, 2] = (y / img_size[1]) * 255
        # Alpha channel - radial gradient for smooth transitions
        distance_to_center = np.sqrt((x - img_size[0] / 2) ** 2 + (y - img_size[1] / 2) ** 2)
        max_distance = np.sqrt((img_size[0] / 2) ** 2 + (img_size[1] / 2) ** 2)
        img[y, x, 3] = (1 - distance_to_center / max_distance) * 255

# Save the generated image
output_path = './tmp/alpha_channel_example.png'
Image.fromarray(img).save(output_path)

# Optionally, display the image
plt.imshow(img)
plt.show()
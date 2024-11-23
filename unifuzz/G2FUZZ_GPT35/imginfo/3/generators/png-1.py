import numpy as np
import matplotlib.pyplot as plt

# Generating a simple image
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Display the image
plt.imshow(image_data)
plt.axis('off')

# Save the image as a PNG file
plt.savefig('./tmp/lossless_compression.png', format='png', bbox_inches='tight', pad_inches=0)

plt.show()
import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with JPG compression to induce artifacting
image.save("./tmp/artifact.jpg", quality=10)
import numpy as np
from PIL import Image

# Create a random image
width = 100
height = 100
image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Save the image as a jpg file
image_path = './tmp/edited_image.jpg'
edited_image = Image.fromarray(image)
edited_image.save(image_path)

print(f"Image saved to {image_path}")
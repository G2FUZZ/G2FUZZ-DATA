import os
from PIL import Image
import numpy as np

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generating a large BMP file
# Define image size (width, height)
# A larger resolution will produce a larger file size. Adjust these values if needed.
width, height = 4000, 4000

# Generate an array of random colors
# Each pixel has 3 components (R, G, B), and each component's value ranges from 0 to 255
random_image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create an image object from the array
image = Image.fromarray(random_image_data)

# Save the image as BMP
image_path = os.path.join(output_dir, 'large_image.bmp')
image.save(image_path)

print(f"Generated BMP image saved at {image_path}")
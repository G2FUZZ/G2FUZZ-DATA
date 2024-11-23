import os
from PIL import Image
import numpy as np

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Define the dimensions of the image
width, height = 100, 100

# Generate a simple image array
# Since PNM does not support alpha channels, we'll use RGB format
# Initialize a numpy array with random colors
image_data = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

# Create an image object using PIL
image = Image.fromarray(image_data, 'RGB')

# Save the image as PNM format
# PNM is a family of formats, we'll use PPM (Portable PixMap) which is colored and supported by PIL under the mode 'PPM'
image.save('./tmp/generated_image.ppm')

print("PNM file generated and saved to ./tmp/generated_image.ppm")
from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image dimensions
width, height = 800, 600

# Generating a gradient image to demonstrate the 24-bit color depth
def generate_gradient(width, height):
    # Initialize an array for the image data
    array = np.zeros((height, width, 3), dtype=np.uint8)

    # Generate gradient
    for y in range(height):
        for x in range(width):
            array[y, x] = [int((x/width)*255), int((y/height)*255), int(((x/width)*(y/height))*255)]
    
    return array

# Generate the image data
img_data = generate_gradient(width, height)

# Create and save the image
img = Image.fromarray(img_data, 'RGB')
img.save('./tmp/gradient_24bit.jpg')

print("The image demonstrating 24-bit color depth has been saved to ./tmp/gradient_24bit.jpg")
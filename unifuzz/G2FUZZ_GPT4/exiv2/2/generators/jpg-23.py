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
# When saving the image, specify the 'optimize' option to False and 'progressive' to True.
# The 'progressive' option can offer a form of error resilience by enabling the image to be
# partially displayed while it is being downloaded, which might help in some error scenarios.
# Note: The JPEG format inherently includes some error resilience features, but the PIL library 
# does not expose direct control over restart intervals or other deeper JPEG encoding parameters.
img.save('./tmp/gradient_24bit_error_resilience.jpg', 'JPEG', quality=95, optimize=False, progressive=True)

print("The image demonstrating 24-bit color depth with error resilience modes has been saved to ./tmp/gradient_24bit_error_resilience.jpg")
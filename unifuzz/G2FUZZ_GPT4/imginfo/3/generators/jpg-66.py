import numpy as np
import cv2
import os
from datetime import datetime

def create_complex_gradient_image():
    # Ensure the base directory exists
    base_dir = './tmp/'
    os.makedirs(base_dir, exist_ok=True)
    
    # Generate a directory path based on the current date and time
    now = datetime.now()
    dir_path = now.strftime(base_dir + "%Y/%m/%d/%H/")
    os.makedirs(dir_path, exist_ok=True)
    
    # Generate an image with 24-bit color depth
    width, height = 256, 256
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Fill the image with a complex gradient
    for y in range(height):
        for x in range(width):
            image[y, x] = [(x+y) % 256, abs(x-y) % 256, (x*y) % 256]
    
    # Save the image with a timestamp in the generated directory
    filename = now.strftime("%Y%m%d_%H%M%S") + '_gradient_image.jpg'
    cv2.imwrite(os.path.join(dir_path, filename), image)
    print(f"Image saved as {os.path.join(dir_path, filename)}")

create_complex_gradient_image()
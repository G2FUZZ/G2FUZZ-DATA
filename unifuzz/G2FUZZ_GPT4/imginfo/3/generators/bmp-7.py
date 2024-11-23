import os
import numpy as np
from PIL import Image

def create_large_bmp(save_path, width, height):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Generate an array of random colors (RGB)
    # Each color channel can range from 0 to 255
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Create an image from the array
    image = Image.fromarray(data, 'RGB')
    
    # Save the image as BMP
    image.save(save_path)

# Example usage
create_large_bmp('./tmp/large_image.bmp', 8000, 8000)  # Create an 8000x8000 BMP image
import os
import numpy as np
from PIL import Image

def create_pyramidal_tiff(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create a sample image (let's create a simple gradient for demonstration)
    width, height = 1024, 1024  # Starting resolution
    base_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Creating a gradient effect for visualization
    for x in range(width):
        for y in range(height):
            base_image[y, x] = [x % 256, y % 256, (x+y) % 256]
    
    # Convert numpy array to PIL Image
    img = Image.fromarray(base_image)
    
    # Save the image in TIFF format with pyramidal levels
    img.save(output_path, format='TIFF', save_all=True,
             append_images=[img.resize((width // (2**i), height // (2**i)), Image.ANTIALIAS)
                            for i in range(1, 5)])  # Creating 4 lower resolutions

create_pyramidal_tiff('./tmp/pyramidal_tiff.tiff')
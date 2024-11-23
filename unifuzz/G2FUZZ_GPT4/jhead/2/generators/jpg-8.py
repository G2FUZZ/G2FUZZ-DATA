import numpy as np
from PIL import Image
import os

def create_blocky_image(image_size=(256, 256), block_size=(8, 8), output_path='./tmp/blocky_compression.jpg'):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create an empty image
    image = np.zeros((image_size[0], image_size[1], 3), dtype=np.uint8)
    
    # Generate blocks with varying colors
    for y in range(0, image_size[0], block_size[0]):
        for x in range(0, image_size[1], block_size[1]):
            # Random color for each block
            block_color = np.random.randint(0, 255, (3,), dtype=np.uint8)
            image[y:y+block_size[0], x:x+block_size[1]] = block_color
    
    # Convert to PIL image and save with high compression (low quality)
    pil_img = Image.fromarray(image)
    pil_img.save(output_path, quality=10)  # Lower quality value increases compression artifacts

create_blocky_image()
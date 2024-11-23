import os
from PIL import Image
import numpy as np

def create_png_file(file_path, width, height):
    # Create a random image array with the given dimensions
    # Using a grayscale image (mode 'L') ranging from 0 (black) to 255 (white)
    img_array = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    
    # Convert the array into an image
    img = Image.fromarray(img_array, mode='L')
    
    # Save the image in PNG format
    img.save(file_path, format='PNG')

# Directory where the PNG files will be saved
save_dir = './tmp/'
os.makedirs(save_dir, exist_ok=True)

# Example: Generate and save a few PNG files with various dimensions
dimensions = [
    (100, 100),  # Small image
    (1000, 1000),  # Medium image
    (5000, 5000)  # Large image
]

for i, (width, height) in enumerate(dimensions, start=1):
    file_path = os.path.join(save_dir, f'image_{i}.png')  # Change the extension to .png
    create_png_file(file_path, width, height)

print("PNG files generated successfully.")
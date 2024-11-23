import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define color depths to generate images for
color_depths = [8, 24]

# Generate an image for each color depth
for bits in color_depths:
    # Calculate the number of colors per channel based on the color depth
    colors_per_channel = 2**(bits // 3)  # Assuming RGB color space for simplicity
    
    # Create a gradient image for each color channel
    width, height = 256, 256  # Example dimensions
    img_data = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Creating a gradient for each channel
    for channel in range(3):
        channel_gradient = np.linspace(0, colors_per_channel-1, num=width, dtype=np.uint8)
        img_data[:, :, channel] = channel_gradient
    
    # Convert the NumPy array to an image
    img = Image.fromarray(img_data, 'RGB')
    
    # If the bit depth is 8, convert the image to "P" mode (palette-based 8-bit pixels)
    if bits == 8:
        img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    
    # Save the image
    file_path = f'./tmp/gradient_{bits}bit.png'
    img.save(file_path)
    print(f"Generated and saved: {file_path}")
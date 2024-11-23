import numpy as np
from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate and save an image with specified bit depth
def generate_image_with_bit_depth(bit_depth, width=256, height=256):
    # Calculate the maximum value for the given bit depth
    max_val = 2**bit_depth - 1
    
    # Generate a gradient image
    gradient = np.tile(np.linspace(0, max_val, width, dtype=np.uint16), (height, 1))
    
    if bit_depth == 8:
        # For 8-bit, we use L mode which is 8-bit pixels, black and white
        image = Image.fromarray(gradient.astype(np.uint8), 'L')
    elif bit_depth == 16:
        # PIL doesn't support 16-bit grayscale directly in a way that's easily saved to common formats,
        # so we'll demonstrate by converting to an RGB image, though this isn't a true 16-bit depth image.
        # This is for demonstration purposes.
        gradient_rgb = np.stack([gradient] * 3, axis=-1)  # Convert to RGB format
        image = Image.fromarray(gradient_rgb.astype(np.uint16), 'RGB')
    elif bit_depth == 24:
        # For 24-bit, we use RGB mode. Each channel (R, G, B) is 8 bits, so total 24 bits per pixel.
        gradient_rgb = np.stack([gradient // 256] * 3, axis=-1)  # Simple conversion for demonstration
        image = Image.fromarray(gradient_rgb.astype(np.uint8), 'RGB')
    else:
        raise ValueError("Unsupported bit depth")
    
    # Save the image
    file_path = f'./tmp/image_{bit_depth}bit.png'
    image.save(file_path)
    print(f"Saved {file_path}")

# Generate images for 8-bit, 16-bit, and 24-bit depths
generate_image_with_bit_depth(8)
generate_image_with_bit_depth(16)
generate_image_with_bit_depth(24)
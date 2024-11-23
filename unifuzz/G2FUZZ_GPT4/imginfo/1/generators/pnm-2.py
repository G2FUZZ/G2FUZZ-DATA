import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to generate a gradient image of specified bit depth
def generate_gradient_image(width, height, bit_depth):
    # Initialize max_value for all paths
    max_value = 2**bit_depth - 1  # Move this line outside the if-else block
    
    # Generate a horizontal gradient
    if bit_depth == 1:
        # For 1-bit depth, generate an image with black and white stripes
        img = np.tile(np.array([0, 255], dtype=np.uint8), width // 2)
    else:
        # Generate a horizontal gradient for other bit depths
        img = np.linspace(0, max_value, width, endpoint=True, dtype=np.uint16 if bit_depth > 8 else np.uint8)
    
    # Repeat the gradient for the height of the image to create a 2D image
    img = np.tile(img, (height, 1))
    return img, max_value

# Function to save the image as PNM
def save_pnm(filename, img, max_value):
    height, width = img.shape
    bit_depth = img.dtype.itemsize * 8
    with open(filename, 'wb') as f:
        if bit_depth == 1 or bit_depth == 8:
            # P5 denotes a grayscale (binary) PNM file
            header = f"P5\n{width} {height}\n{max_value}\n".encode()
        else:
            # For 16-bit, still use P5 but with max_value to indicate depth
            header = f"P5\n{width} {height}\n{max_value}\n".encode()
        f.write(header)
        img.tofile(f)

# Parameters
width, height = 256, 256  # Image dimensions
bit_depths = [1, 8, 16]  # Bit depths for demonstration

# Generate and save PNM files for each bit depth
for bit_depth in bit_depths:
    img, max_value = generate_gradient_image(width, height, bit_depth)
    filename = os.path.join(output_dir, f'gradient_{bit_depth}bit.pgm')
    save_pnm(filename, img, max_value)

print("PNM files generated.")
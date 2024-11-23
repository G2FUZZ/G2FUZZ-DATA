import numpy as np
import struct

# Function to generate a sample TGA file with color correction information
def generate_tga_with_color_correction(file_name):
    # Create a sample color map
    color_map = np.random.randint(0, 256, size=(256, 3), dtype=np.uint8)
    
    # Create a sample gamma correction value
    gamma_correction = np.random.uniform(0.5, 2.0)
    
    # Save color correction information to the TGA file
    with open(file_name, 'wb') as f:
        f.write(b'\x00\x00\x02')  # Image type - color-mapped image
        f.write(b'\x00\x00\x01')  # Color map type - no color map included
        f.write(b'\x00\x00')  # Image specification - no color map
        f.write(color_map.tobytes())  # Color map data
        f.write(struct.pack('f', gamma_correction))  # Convert gamma_correction to bytes

# Generate a sample TGA file with color correction information
file_name = './tmp/sample_color_correction.tga'
generate_tga_with_color_correction(file_name)
print(f'TGA file with color correction information generated: {file_name}')
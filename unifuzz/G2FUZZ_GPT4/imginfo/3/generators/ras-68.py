import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image resolution
width, height = 256, 256

# Generate a more complex raster image with a circular gradient
image_data = np.zeros((height, width, 3), dtype=np.uint8)
center_x, center_y = width // 2, height // 2
radius = min(center_x, center_y, 100)

for y in range(height):
    for x in range(width):
        # Calculate distance to the center
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        # Generate a circular gradient
        if distance < radius:
            intensity = int((1 - distance / radius) * 255)
            image_data[y, x] = [intensity, intensity, 255 - intensity]
        else:
            image_data[y, x] = [0, 0, 128]  # Background color

# Function to save image data as a .ras file
def save_ras(filename, data):
    height, width, depth = data.shape
    assert depth == 3, "Only RGB images are supported for RAS format."
    
    # RAS header structure: magic (4 bytes), width (4 bytes), height (4 bytes),
    # depth (4 bytes), length (4 bytes), type (4 bytes), maptype (4 bytes),
    # maplength (4 bytes)
    magic = 0x59a66a95  # Magic number for Sun Raster files
    ras_type = 1  # Type of RAS file; 1 for standard
    maptype = 0  # Color map type; 0 for no color map
    maplength = 0  # Length of color map; 0 for no color map
    depth = 24  # Depth (24 for RGB)
    length = width * height * depth // 8  # Length of the image data in bytes
    
    header = np.array([magic, width, height, depth, length, ras_type, maptype, maplength], dtype=np.uint32).byteswap().tobytes()
    
    # Flatten the image data to match RAS format requirements
    image_bytes = data.flatten().tobytes()
    
    # Write the header and image data to a file
    with open(filename, 'wb') as file:
        file.write(header)
        file.write(image_bytes)

# Save the image as a .ras file
save_ras('./tmp/complex_example.ras', image_data)
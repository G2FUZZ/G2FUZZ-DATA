import os
import struct

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a simple RAS file
def create_ras_file(file_path, width, height, depth=24):
    magic_number = 0x6a95  # Magic number for RAS files
    length = width * height * (depth // 8)  # Calculate the data size
    rtype = 1  # Type of file; 1 indicates standard, uncompressed
    maptype = 0  # Type of colormap; 0 indicates no colormap
    maplength = 0  # Length of colormap; 0 when no colormap is used
    
    # Open the file to write binary data
    with open(file_path, 'wb') as file:
        # Write header information
        file.write(struct.pack('>IIIIII', magic_number, width, height, depth, length, rtype))
        file.write(struct.pack('>II', maptype, maplength))
        
        # Generate a simple image data (black image for simplicity)
        for _ in range(height):
            for _ in range(width):
                if depth == 24:
                    # Write a black pixel (R, G, B)
                    file.write(struct.pack('BBB', 0, 0, 0))
                elif depth == 8:
                    # Write a black pixel in grayscale
                    file.write(struct.pack('B', 0))
                # Add more depth cases as needed

# Example usage: Create a 100x100 black RAS image
create_ras_file('./tmp/example.ras', 100, 100, 24)
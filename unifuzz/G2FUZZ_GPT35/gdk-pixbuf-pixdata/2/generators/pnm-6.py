import os

# Function to create a PNM file with given features
def create_pnm_file(filename, width, height, max_val, image_data):
    header = f"P6\n{width} {height}\n{max_val}\n"
    with open(filename, 'wb') as file:
        file.write(bytearray(header, 'ascii'))
        file.write(bytearray(image_data))

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Define image properties
width = 100
height = 100
max_val = 255

# Generate random image data
import numpy as np
image_data = np.random.randint(0, max_val + 1, (width * height * 3), dtype=np.uint8)

# Save the generated PNM file
filename = './tmp/generated_image.pnm'
create_pnm_file(filename, width, height, max_val, image_data)

print(f"PNM file '{filename}' has been generated successfully.")
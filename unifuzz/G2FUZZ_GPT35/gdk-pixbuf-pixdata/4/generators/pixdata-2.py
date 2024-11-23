import numpy as np
import os

# Generate some random image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the image data into a file
file_path = os.path.join(directory, 'pixdata.txt')
np.savetxt(file_path, image_data.flatten())

print(f"File saved to: {file_path}")
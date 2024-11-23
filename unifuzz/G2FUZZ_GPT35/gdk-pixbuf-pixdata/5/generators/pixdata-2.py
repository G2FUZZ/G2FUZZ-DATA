import numpy as np
import os

# Create a folder if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate random pixel values as image data
image_data = np.random.randint(0, 256, size=(100, 100))

# Save the image data to a .pixdata file
file_path = './tmp/image_data.pixdata'
np.savetxt(file_path, image_data, fmt='%d')

print(f"Image data saved to: {file_path}")
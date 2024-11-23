import numpy as np

# Create pixel data for the 'ras' file
pixel_data = np.random.randint(0, 255, size=(100, 100))

# Save the pixel data to a file
file_path = './tmp/pixel_data.ras'
with open(file_path, 'wb') as file:
    file.write(pixel_data.astype(np.uint8).tobytes())

print(f"Pixel data saved to {file_path}")
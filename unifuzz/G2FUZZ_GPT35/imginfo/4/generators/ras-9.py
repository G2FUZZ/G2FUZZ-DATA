import numpy as np

# Generate pixel data for the 'ras' file
pixel_data = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)

# Save the pixel data as a 'ras' file in the ./tmp/ directory
file_path = './tmp/generated_file.ras'
with open(file_path, 'wb') as file:
    file.write(pixel_data.tobytes())

print(f"File saved successfully at: {file_path}")
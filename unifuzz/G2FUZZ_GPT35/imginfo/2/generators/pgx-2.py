import numpy as np

# Generate random image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Save the generated image data to a '.pgx' file
file_path = './tmp/image_data.pgx'
with open(file_path, 'wb') as file:
    file.write(image_data.tobytes())

print(f"Image data saved to '{file_path}' successfully.")
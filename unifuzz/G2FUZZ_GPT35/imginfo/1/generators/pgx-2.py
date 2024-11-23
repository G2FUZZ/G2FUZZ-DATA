import numpy as np

# Generate random image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Save image data to a pgx file
file_path = './tmp/image.pgx'
with open(file_path, 'wb') as file:
    file.write(image_data.tobytes())

print(f"Saved image data to {file_path}")
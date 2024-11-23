import numpy as np

def save_pnm_file(file_path, image_data):
    with open(file_path, 'wb') as f:
        f.write(image_data)

# Generate PNM file data
width, height = 100, 100
max_val = 255
image_data = np.random.randint(0, max_val, (height, width, 3), dtype=np.uint8)

# Create P6 PNM file format data
pnm_data = bytearray()
pnm_data.extend(b'P6\n')
pnm_data.extend(f'{width} {height}\n'.encode())
pnm_data.extend(f'{max_val}\n'.encode())
pnm_data.extend(image_data.tobytes())

# Save PNM file
file_path = './tmp/sample.pnm'
save_pnm_file(file_path, pnm_data)

print(f'PNM file saved at: {file_path}')
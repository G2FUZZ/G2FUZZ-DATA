import numpy as np

# Function to create a PNM file with limited metadata
def create_pnm_file(file_path):
    width, height = 100, 100
    max_val = 255
    image_data = np.random.randint(0, max_val + 1, (height, width), dtype=np.uint8)

    with open(file_path, 'wb') as f:
        f.write(b'P5\n')
        f.write(f'{width} {height}\n'.encode())
        f.write(f'{max_val}\n'.encode())
        f.write(image_data.tobytes())

file_path = './tmp/image.pgm'
create_pnm_file(file_path)
print(f'PNM file with limited metadata created and saved at: {file_path}')
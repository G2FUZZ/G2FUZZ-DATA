import numpy as np

def create_pnm_file(file_path, image_data):
    with open(file_path, 'wb') as f:
        f.write(b'P6\n')
        f.write(b'# Lossless: The PNM format is lossless, meaning it retains all the original image data without compression artifacts.\n')
        f.write(f'{image_data.shape[1]} {image_data.shape[0]}\n'.encode())
        f.write(b'255\n')
        f.write(image_data.astype(np.uint8).tobytes())

image_data = np.random.randint(0, 256, size=(100, 100, 3))
file_path = './tmp/sample_image.pnm'
create_pnm_file(file_path, image_data)
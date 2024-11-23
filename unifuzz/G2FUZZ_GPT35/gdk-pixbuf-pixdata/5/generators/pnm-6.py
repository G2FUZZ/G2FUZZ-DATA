import numpy as np

def create_pnm_file(filename, image_data):
    with open(filename, 'wb') as f:
        f.write(b'P5\n')
        f.write(f'{image_data.shape[1]} {image_data.shape[0]}\n'.encode())
        f.write(b'255\n')
        f.write(image_data.astype(np.uint8).tobytes())

image_data = np.random.randint(0, 256, (100, 100))  # Random image data
filename = './tmp/sample_image.pgm'
create_pnm_file(filename, image_data)
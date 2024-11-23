import numpy as np
from PIL import Image
import os

def run_length_encode(image):
    flat = image.flatten()
    result = []
    current_run_value = flat[0]
    current_run_length = 1
    for val in flat[1:]:
        if val == current_run_value:
            current_run_length += 1
        else:
            result.append((current_run_length, current_run_value))
            current_run_value = val
            current_run_length = 1
    result.append((current_run_length, current_run_value))
    return result

def save_ras_rle_compressed(image, filename):
    encoded = run_length_encode(image)
    with open(filename, 'wb') as file:
        file.write(b'RAS')  # Simple identifier, not part of the actual RAS spec
        width, height = image.shape
        file.write(width.to_bytes(4, 'big'))
        file.write(height.to_bytes(4, 'big'))
        for length, value in encoded:
            file.write(length.to_bytes(4, 'big'))
            file.write(int(value).to_bytes(1, 'big'))  # Convert numpy.uint8 to int

def create_and_save_compressed_ras():
    width, height = 100, 50
    image = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            if (x // 10) % 2 == (y // 10) % 2:
                image[y, x] = 255

    img = Image.fromarray(image)
    img.save('./tmp/test_image.png')

    save_ras_rle_compressed(image, './tmp/test_image_compressed.ras')

if __name__ == '__main__':
    os.makedirs('./tmp/', exist_ok=True)
    create_and_save_compressed_ras()
import numpy as np
from PIL import Image
import os

def run_length_encode(image):
    if len(image.shape) == 3:
        # For RGB images, flatten the array in a way that keeps color channels together per pixel
        flat = image.reshape(-1, 3)
        is_rgb = True
    else:
        flat = image.flatten()
        is_rgb = False

    result = []
    current_run_value = flat[0]
    current_run_length = 1
    
    for val in flat[1:]:
        if np.array_equal(val, current_run_value):
            current_run_length += 1
        else:
            result.append((current_run_length, current_run_value))
            current_run_value = val
            current_run_length = 1
    result.append((current_run_length, current_run_value))
    
    return result, is_rgb

def save_ras_rle_compressed(image, filename):
    encoded, is_rgb = run_length_encode(image)
    
    with open(filename, 'wb') as file:
        file.write(b'RAS')  # Simple identifier, not part of the actual RAS spec
        height, width = image.shape[:2]
        color_depth = 3 if is_rgb else 1  # 3 for RGB, 1 for grayscale
        file.write(width.to_bytes(4, 'big'))
        file.write(height.to_bytes(4, 'big'))
        file.write(color_depth.to_bytes(1, 'big'))  # Adding color depth to the file
        
        for length, value in encoded:
            file.write(length.to_bytes(4, 'big'))
            if is_rgb:
                # For RGB, convert each value in the tuple to bytes
                for val in value:
                    file.write(int(val).to_bytes(1, 'big'))
            else:
                file.write(int(value).to_bytes(1, 'big'))  # Convert numpy.uint8 to int if grayscale

def create_and_save_compressed_ras():
    width, height = 100, 50
    # Creating a checkerboard pattern for an RGB image
    image_rgb = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            if (x // 10) % 2 == (y // 10) % 2:
                image_rgb[y, x] = [255, 0, 0]  # Red squares
            else:
                image_rgb[y, x] = [0, 255, 0]  # Green squares

    img_rgb = Image.fromarray(image_rgb)
    img_rgb.save('./tmp/test_image_rgb.png')

    save_ras_rle_compressed(image_rgb, './tmp/test_image_rgb_compressed.ras')

if __name__ == '__main__':
    os.makedirs('./tmp/', exist_ok=True)
    create_and_save_compressed_ras()
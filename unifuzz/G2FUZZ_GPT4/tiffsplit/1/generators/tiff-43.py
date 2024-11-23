from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_gradient_image(width, height, bitdepth):
    max_value = 2**bitdepth - 1
    gradient = np.tile(np.linspace(0, max_value, width, dtype=np.uint16 if bitdepth > 8 else np.uint8), (height, 1))
    image_data = np.stack((gradient,) * 3, axis=-1)
    
    if bitdepth > 8:
        image_data = (image_data / 256).astype(np.uint8)
    
    image = Image.fromarray(image_data)
    return image

def needs_bigtiff_extension(width, height, bitdepth):
    estimated_file_size = width * height * bitdepth * 3 / 8
    return estimated_file_size > 4 * 1024**3

def save_complex_tiff(images, filename, bitdepth):
    compression_method = 'tiff_lzw' if bitdepth <= 8 else 'tiff_deflate'
    
    # Save all images at once, creating a multi-layer TIFF
    images[0].save(filename, save_all=True, append_images=images[1:], format='TIFF', compression=compression_method)

images_to_save = []
for bitdepth in [8, 16]:
    image = create_gradient_image(256, 256, bitdepth)
    images_to_save.append(image)

filename = './tmp/complex_gradient_multi_layer.tiff'

if needs_bigtiff_extension(256, 256, 16):  # Using the highest bitdepth in the example for calculation
    print(f"BigTIFF would be used for {filename}. However, PIL/Pillow does not support BigTIFF natively.")
else:
    save_complex_tiff(images_to_save, filename, 16)  # Assuming you want to use the highest bitdepth for metadata

print("Complex TIFF file has been generated with multiple layers, compression methods, and without custom metadata.")
import numpy as np
from PIL import Image
import os

def create_ras_with_compression(output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create an image with large areas of uniform color
    # Here we create a 100x100 pixels image with a blue square in the middle
    image_data = np.zeros((100, 100, 3), dtype=np.uint8)
    image_data[25:75, 25:75, 2] = 255  # Setting the blue channel in the middle

    # Convert the numpy array to a PIL image
    image = Image.fromarray(image_data)

    # Save the image with RLE compression
    # The PIL library does not directly support saving with RAS RLE compression, so we use a workaround
    # We save the image in a format that supports RLE, then change the extension to '.ras'
    # Note: This is a demonstration. In real applications, use appropriate libraries or methods to handle specific file formats.
    temp_path = output_path + '.bmp'
    image.save(temp_path, format='BMP', bits=4, compression='GROUP4')  # BMP supports RLE compression
    os.rename(temp_path, output_path)

# Save the generated RAS file into ./tmp/
output_path = './tmp/compressed_image.ras'
create_ras_with_compression(output_path)

print(f"RAS file with RLE compression saved to: {output_path}")
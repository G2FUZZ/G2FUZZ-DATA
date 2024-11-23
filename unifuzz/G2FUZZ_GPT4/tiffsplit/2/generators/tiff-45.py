import numpy as np
import tifffile as tiff
import os
from skimage.color import gray2rgb
from matplotlib import cm
from datetime import datetime

# Ensure the output directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define image properties
image_width, image_height = 256, 256  # dimensions in pixels
layers = 3  # Number of layers in the TIFF
bit_depth = 16  # 16 bits per pixel for detailed images
resolution = (300, 300)  # resolution in DPI (dots per inch)

# Function to generate a layer with a specific pattern
def generate_pattern(layer_id, width, height):
    if layer_id == 0:  # Horizontal gradient
        layer = np.linspace(0, 2**bit_depth-1, num=width, dtype=np.uint16)
        layer = np.tile(layer, (height, 1))
    elif layer_id == 1:  # Vertical gradient
        layer = np.linspace(0, 2**bit_depth-1, num=height, dtype=np.uint16)
        layer = np.tile(layer[:, None], (1, width))
    else:  # Diagonal gradient
        layer = np.linspace(0, 2**bit_depth-1, num=height, dtype=np.uint16)
        layer = np.diag(layer)
        layer = np.tile(layer, (int(np.ceil(height/layer.shape[0])), int(np.ceil(width/layer.shape[1]))))
        layer = layer[:height, :width]
    return layer

# Generate layers with different patterns
layers_list = [generate_pattern(i, image_width, image_height) for i in range(layers)]

# Convert layers to RGB using different color maps
color_maps = [cm.viridis, cm.plasma, cm.inferno]
layers_rgb = [color_maps[i](layers_list[i] / np.max(layers_list[i])) for i in range(layers)]

# Save the image as a TIFF file with specified resolutions, layers, and metadata
tiff_file_path = os.path.join(output_dir, "complex_generated_image.tiff")

# Metadata
metadata = {
    'Software': 'NumPy, tifffile, and skimage',
    'DateTime': datetime.now().strftime("%Y:%m:%d %H:%M:%S"),
    'ImageDescription': 'A complex TIFF file with multiple layers and different patterns',
}

# Save the multilayer TIFF
with tiff.TiffWriter(tiff_file_path, bigtiff=True) as tif:
    for layer in layers_rgb:
        # Convert float images to uint8 for saving
        layer_uint8 = (layer[:, :, :3] * 255).astype(np.uint8)
        tif.write(layer_uint8, resolution=(resolution[0], resolution[1], 'INCH'), metadata=metadata, photometric='rgb')

print(f"Complex TIFF file saved at: {tiff_file_path}")
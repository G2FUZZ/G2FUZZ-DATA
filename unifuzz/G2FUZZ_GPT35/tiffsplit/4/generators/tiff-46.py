import numpy as np
import tifffile as tf

# Create a sample image with multiple layers
image_layer1 = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image_layer2 = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
image_layers = [image_layer1, image_layer2]

# Set the resolution unit to centimeters (2) instead of default inches (1)
resolution_unit = 2
image_resolution = (300, 300)  # 300 pixels per inch

# Save the image as a TIFF file with 'deflate' compression, resolution units, and custom metadata
metadata = {'Author': 'John Doe', 'CreationDate': '2022-08-25'}
tf.imwrite('./tmp/sample_image_with_complex_features.tiff', image_layers, compress='deflate', resolution=(resolution_unit, image_resolution), extratags=[(40091, 3, 1, 234, False), (40092, 3, 1, 178, False), (40093, 7, 1, 111, metadata)])

print("TIFF file with Complex Features saved successfully.")
import numpy as np
import tifffile as tf

# Create a simple image data
image_data = np.random.randint(0, 255, size=(512, 512), dtype=np.uint8)

# Save the image data as a TIFF file in BigTIFF format
file_path = './tmp/big_tiff_file.tiff'
tf.imwrite(file_path, image_data, bigtiff=True)

print(f"BigTIFF file saved at: {file_path}")
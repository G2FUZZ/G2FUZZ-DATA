import numpy as np
import tifffile as tf
from tifffile.tifffile import TIFF

# Create a sample image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Save the image data as a TIFF file with Embedded ICC Profiles
file_path = "./tmp/sample_image_with_icc.tiff"
tf.imwrite(file_path, image_data, photometric='rgb', description="Embedded ICC Profiles: TIFF files can embed ICC profiles to ensure accurate color reproduction and color management across different devices and platforms.")

print(f"TIFF file with Embedded ICC Profiles saved at: {file_path}")
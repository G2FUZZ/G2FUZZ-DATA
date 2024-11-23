import numpy as np
import tifffile as tf

# Create a sample image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Save the image data as a TIFF file
file_path = "./tmp/sample_image.tiff"
tf.imwrite(file_path, image_data)

print(f"TIFF file saved at: {file_path}")
import numpy as np
import tifffile as tf

# Create a sample image
image = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Set additional file features
resolution = (300, 300)  # Set resolution to 300 dpi
metadata = {'author': 'Jane Smith', 'description': 'Sample image for demonstration'}  # Add metadata information

# Save the image as a TIFF file with additional file features
tf.imwrite('./tmp/sample_image_complex.tiff', image, compress='deflate', resolution=resolution, metadata=metadata)

print("TIFF file with Deflate compression and additional features saved successfully.")
import numpy as np
import tifffile as tf

# Create a sample image
image = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Set the resolution unit to centimeters (2) instead of default inches (1)
resolution_unit = 2
image_resolution = (300, 300)  # 300 pixels per inch

# Save the image as a TIFF file with 'deflate' compression and resolution units
tf.imwrite('./tmp/sample_image_with_resolution_units.tiff', image, compress='deflate', resolution=(resolution_unit, image_resolution))

print("TIFF file with Image Resolution Units saved successfully.")
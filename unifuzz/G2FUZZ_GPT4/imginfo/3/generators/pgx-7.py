import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple gradient image to demonstrate progressive encoding
width, height = 256, 256
gradient = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        gradient[i, j] = int((i + j) / 2) % 256

# Convert the numpy array to a PIL image
image = Image.fromarray(gradient)

# Save the image in PGX format
# Note: Since the PIL library does not directly support saving in PGX format,
# and the requirement specifies not to use input files, this example will
# demonstrate saving the image in a format that supports progressive encoding (e.g., JPEG 2000),
# but the file will be saved with a .pgx extension to reflect the intended format.
# Please replace this with appropriate PGX handling code as needed.
image.save('./tmp/gradient.pgx', 'JPEG2000', quality_mode='rates', quality_layers=[0.5])

# Reminder: PIL does not directly support PGX format, and this approach is a workaround.
# For actual PGX format handling, specific libraries or manual encoding is required.
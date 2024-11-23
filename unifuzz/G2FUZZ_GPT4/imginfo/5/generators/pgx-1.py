from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a grayscale image of 256x256 pixels
width, height = 256, 256
image = Image.fromarray(np.zeros((height, width), dtype=np.uint8), 'L')

# Optionally, manipulate the image here (this step is skipped in this example)

# Save the image as a PGX file
pgx_filename = os.path.join(output_dir, 'image.pgx')
image.save(pgx_filename, format='JPEG2000', quality_mode='dB', quality_layers=[80])

print(f'PGX file saved as {pgx_filename}')
import os
import numpy as np

# Create a directory for the output file if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the image dimensions and create a gradient
width, height = 256, 256  # Example dimensions
image = np.zeros((height, width), dtype=np.uint16)

# Creating a vertical gradient
for x in range(width):
    for y in range(height):
        image[y, x] = int((x / width) * 65535)  # Scale the gradient to 16-bit

# Function to save the image as a PGX file
def save_as_pgx(image, file_path):
    with open(file_path, 'wb') as f:
        # PGX header: we define it for a 16-bit, big-endian grayscale image
        # PGX does not have a standard header, but we'll use this for simplicity
        header = b'PG ML + 65535 16B\n'
        f.write(header)
        # Ensure the image data is in big-endian format
        if image.dtype.byteorder == '<' or (image.dtype.byteorder == '=' and os.sys.byteorder == 'little'):
            big_endian_image = image.byteswap().newbyteorder()
        else:
            big_endian_image = image
        # Writing the image data
        for y in range(big_endian_image.shape[0]):
            for x in range(big_endian_image.shape[1]):
                # Convert the pixel value to bytes and write it
                f.write(big_endian_image[y, x].tobytes())

# Save the gradient image as a PGX file
pgx_file_path = os.path.join(output_dir, 'gradient.pgx')
save_as_pgx(image, pgx_file_path)

print(f'Gradient PGX file saved to {pgx_file_path}')
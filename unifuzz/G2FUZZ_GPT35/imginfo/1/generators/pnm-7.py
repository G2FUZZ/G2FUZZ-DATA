import numpy as np

# Function to save a matrix as a PNM file
def save_pnm_file(matrix, filename):
    height, width = matrix.shape
    with open(filename, 'wb') as f:
        f.write('P5\n{} {}\n255\n'.format(width, height).encode('ascii'))
        f.write(matrix.astype(np.uint8).tobytes())

# Generate a random 100x100 matrix as an example image
image = np.random.randint(0, 256, size=(100, 100))

# Save the generated image as a PNM file
save_pnm_file(image, './tmp/generated_image.pgm')
import numpy as np

# Define the dimensions of the image
rows = 100
cols = 100

# Generate random pixel values between 0 and 255
pixels = np.random.randint(256, size=(rows, cols))

# Save the pixel values to a PGM file
with open('./tmp/image.pgm', 'w') as f:
    f.write('P2\n')
    f.write(f'{cols} {rows}\n')
    f.write('255\n')
    for row in pixels:
        f.write(' '.join(map(str, row)) + '\n')
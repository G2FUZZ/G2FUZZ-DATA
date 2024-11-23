import numpy as np

# Define the image dimensions
height = 100
width = 150

# Generate random pixel data
pixel_data = np.random.randint(0, 256, (height, width))

# Save the pixel data to a .pnm file
file_path = './tmp/generated_image.pnm'
with open(file_path, 'w') as file:
    file.write('P2\n')
    file.write(f'{width} {height}\n')
    file.write('255\n')
    for row in pixel_data:
        file.write(' '.join(map(str, row)) + '\n')

print(f'Generated image saved to: {file_path}')
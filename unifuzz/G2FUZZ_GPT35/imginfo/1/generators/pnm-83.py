import numpy as np

# Function to create a PNM file with complex features
def create_complex_pnm_file(filename, width, height, max_val, data):
    with open(filename, 'w') as file:
        file.write('# Complex PNM File\n')
        file.write('P2\n')
        file.write(f'# Image Size: {width}x{height}\n')
        file.write(f'{width} {height}\n')
        file.write(f'# Maximum Pixel Value: {max_val}\n')
        file.write(f'{max_val}\n')
        
        file.write('# Image Data\n')
        for row in data:
            file.write(' '.join(map(str, row)) + '\n')

# Define PNM file features
width = 8
height = 8
max_val = 200
data = np.random.randint(50, max_val, (height, width))

# Save complex PNM file
filename = './tmp/complex.pnm'
create_complex_pnm_file(filename, width, height, max_val, data)

print(f'Complex PNM file with features created and saved as {filename}')
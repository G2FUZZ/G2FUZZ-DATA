import numpy as np

# Function to create a PNM file with the given features
def create_pnm_file(filename, width, height, max_val, data):
    with open(filename, 'w') as file:
        file.write(f'P2\n{width} {height}\n{max_val}\n')
        for row in data:
            file.write(' '.join(map(str, row)) + '\n')

# Define PNM file features
width = 5
height = 5
max_val = 255
data = np.random.randint(0, max_val, (height, width))

# Save PNM file
filename = './tmp/test.pnm'
create_pnm_file(filename, width, height, max_val, data)

print(f'PNM file with features created and saved as {filename}')
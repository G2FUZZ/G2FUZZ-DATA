import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate sample 'ani' files with metadata
for i in range(3):
    filename = f'{directory}ani_{i}.ani'
    with open(filename, 'w') as file:
        file.write(f'Metadata for ani_{i}.ani:\n')
        file.write(f'Frame duration: 0.1 sec\n')
        file.write(f'Dimensions: 640x480\n')
        file.write(f'Color palette: RGB\n')

print('Generated ani files with metadata successfully!')
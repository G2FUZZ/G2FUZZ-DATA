import os

# Create a directory for the files if it doesn't exist
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate ras files with different color spaces
color_spaces = ['RGB', 'CMYK', 'grayscale', 'indexed color']

for idx, color_space in enumerate(color_spaces):
    filename = f'{output_directory}file_{idx}.ras'
    
    with open(filename, 'w') as file:
        file.write(f'Color space: {color_space}\n')
    
    print(f'File {filename} created with color space: {color_space}')
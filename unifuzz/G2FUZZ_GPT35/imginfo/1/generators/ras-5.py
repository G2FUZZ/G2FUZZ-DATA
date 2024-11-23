import os

# Create a directory to save 'ras' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with different color spaces
color_spaces = ['RGB', 'CMYK', 'grayscale']

for color_space in color_spaces:
    file_path = f'./tmp/file_{color_space}.ras'
    with open(file_path, 'w') as file:
        file.write(f'Color Space: {color_space}')

print('Files generated successfully')
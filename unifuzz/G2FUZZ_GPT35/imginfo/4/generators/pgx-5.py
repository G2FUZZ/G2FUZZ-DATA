import os

# Define the color depth options
color_depths = ['grayscale', 'indexed color', 'RGB', 'CMYK']

# Create a directory to store the 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with different color depths
for depth in color_depths:
    file_path = f'./tmp/file_{depth}.pgx'
    with open(file_path, 'w') as file:
        file.write(f'Color Depth: {depth}')
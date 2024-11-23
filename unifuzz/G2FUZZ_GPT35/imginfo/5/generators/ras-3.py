import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with different color depths
color_depths = ['monochrome', 'grayscale', 'indexed color', 'truecolor']

for depth in color_depths:
    file_path = f'./tmp/file_{depth.replace(" ", "_")}.ras'
    with open(file_path, 'w') as file:
        file.write(f'Color Depth: {depth}\n')
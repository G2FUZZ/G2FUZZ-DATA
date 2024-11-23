import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample 'ani' file with color depth information
ani_filename = 'sample.ani'
color_depth = '256 colors'

with open(os.path.join(directory, ani_filename), 'w') as f:
    f.write(f'Color Depth: {color_depth}')

print(f"Generated '{ani_filename}' with Color Depth: {color_depth}")
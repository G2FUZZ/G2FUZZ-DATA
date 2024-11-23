import os

# Create a directory for storing PNM files
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the content for the PNM file with multiple color channels and larger dimensions
content = """P3
# Complex PNM File: This file contains multiple color channels and larger dimensions.
4 4
255
255 0 0 0 255 255 0 0 255 255 0 0 0 255 255
0 255 0 255 0 255 0 255 0 255 0 255 0 255
255 255 0 0 255 255 255 0 0 255 255 0 0 255
255 255 0 0 255 255 255 0 0 255 255 0 0 255
"""

# Save the PNM file
file_path = os.path.join(directory, 'complex_pnm_file.pnm')
with open(file_path, 'w') as file:
    file.write(content)

print(f'Complex PNM file saved at: {file_path}')
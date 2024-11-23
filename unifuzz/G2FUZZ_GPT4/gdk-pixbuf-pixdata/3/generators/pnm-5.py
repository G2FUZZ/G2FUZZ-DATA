import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the new PNM file
file_path = './tmp/example.ppm'

# PPM header for a small 3x2 image
# P3 means this is a RGB color image in ASCII
# 3 2 specifies the width and height, 255 specifies the maximum color value.
header = 'P3\n3 2\n255\n'

# Image data: 6 pixels, each with RGB components.
# This example creates two rows of three pixels:
# First row is red, green, and blue.
# Second row is cyan, magenta, and yellow.
image_data = [
    '255 0 0 ', '0 255 0 ', '0 0 255 ',
    '0 255 255 ', '255 0 255 ', '255 255 0 '
]

# Combine the header and image_data into one string
ppm_content = header + '\n'.join(image_data)

# Write the PPM content to a file
with open(file_path, 'w') as file:
    file.write(ppm_content)

print(f'PPM file saved to {file_path}')
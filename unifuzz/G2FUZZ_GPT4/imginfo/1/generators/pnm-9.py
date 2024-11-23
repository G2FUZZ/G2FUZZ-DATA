import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the new PPM file
output_file_path = os.path.join(output_dir, 'example.ppm')

# PPM header: P3 means this is a RGB color image in ASCII
# 3 2 specifies the width and height
# 255 is the maximum color value
ppm_header = 'P3\n3 2\n255\n'
# Image data: 3x2 image with simple RGB values
# Each row in the comment represents a row in the image
# Red, Green, Blue, Yellow, Magenta, Cyan
ppm_data = '''
255 0 0  0 255 0  0 0 255
255 255 0  255 0 255  0 255 255
'''

# Combine the header and data, then write to the file
ppm_content = ppm_header + ppm_data.strip()
with open(output_file_path, 'w') as file:
    file.write(ppm_content)

print(f'PPM file has been saved to {output_file_path}')
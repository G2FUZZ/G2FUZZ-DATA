import os

# Create a directory to store the generated 'pnm' files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate an example P1 'pnm' file (ASCII format)
p1_file_path = os.path.join(directory, 'example_p1.pbm')
with open(p1_file_path, 'w') as f:
    f.write('P1\n')
    f.write('# Example P1 PBM file\n')
    f.write('4 4\n')
    f.write('1 0 1 0\n')
    f.write('0 1 0 1\n')
    f.write('1 0 1 0\n')
    f.write('0 1 0 1\n')

# Generate an example P6 'pnm' file (Binary format)
p6_file_path = os.path.join(directory, 'example_p6.ppm')
with open(p6_file_path, 'wb') as f:
    f.write(b'P6\n')
    f.write(b'# Example P6 PPM file\n')
    f.write(b'4 4\n')
    f.write(b'255\n')
    for _ in range(16):
        f.write(bytes([255, 0, 255]))  # Purple color

print(f'Files generated and saved in {directory}')
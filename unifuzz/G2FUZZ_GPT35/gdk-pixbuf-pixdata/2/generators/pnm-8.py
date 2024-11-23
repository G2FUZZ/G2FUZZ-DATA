import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate PNM file in ASCII format
with open('./tmp/human_readable.pnm', 'w') as file:
    file.write('P3\n')
    file.write('# This is a PNM file in ASCII format\n')
    file.write('3 2\n')
    file.write('255\n')
    file.write('255 0 0 0 255 0 0 0 255\n')
    file.write('0 255 0 255 0 255 255 255 255\n')

# Generate PNM file in binary format
with open('./tmp/binary.pnm', 'wb') as file:
    file.write(b'P6\n')
    file.write(b'# This is a PNM file in binary format\n')
    file.write(b'3 2\n')
    file.write(b'255\n')
    file.write(bytes([255, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 0, 255, 255, 255, 255, 255]))

print('PNM files generated and saved in ./tmp/')
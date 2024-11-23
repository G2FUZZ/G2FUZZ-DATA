import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# PBM Data - A simple 3x3 checkerboard pattern
pbm_data_ascii = "P1\n3 3\n0 1 0\n1 0 1\n0 1 0"
pbm_data_binary = b"P4\n3 3\n\x90"

# PGM Data - A simple gradient from black to white in 3x3
pgm_data_ascii = "P2\n3 3\n255\n0 127 255\n64 191 255\n128 255 255"
pgm_data_binary = b"P5\n3 3\n255\n\x00\x7F\xFF\x40\xBF\xFF\x80\xFF\xFF"

# PPM Data - A simple 2x2 image with red, green, blue, and white pixels
ppm_data_ascii = "P3\n2 2\n255\n255 0 0 0 255 0\n0 0 255 255 255 255"
ppm_data_binary = b"P6\n2 2\n255\n\xFF\x00\x00\x00\xFF\x00\x00\x00\xFF\xFF\xFF\xFF"

# Function to write data to a file
def write_file(filename, data, binary=False):
    mode = 'wb' if binary else 'w'
    with open(filename, mode) as file:
        file.write(data)

# Write PBM files
write_file('./tmp/pbm_ascii.pbm', pbm_data_ascii)
write_file('./tmp/pbm_binary.pbm', pbm_data_binary, binary=True)

# Write PGM files
write_file('./tmp/pgm_ascii.pgm', pgm_data_ascii)
write_file('./tmp/pgm_binary.pgm', pgm_data_binary, binary=True)

# Write PPM files
write_file('./tmp/ppm_ascii.ppm', ppm_data_ascii)
write_file('./tmp/ppm_binary.ppm', ppm_data_binary, binary=True)

print("PNM files have been generated and saved to ./tmp/")
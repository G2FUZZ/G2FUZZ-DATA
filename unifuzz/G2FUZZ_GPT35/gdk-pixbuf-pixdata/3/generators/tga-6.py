import struct

# Function to create a TGA file with specified origin
def create_tga_file(origin):
    # Define TGA header
    tga_header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    # Set origin based on input
    if origin.lower() == 'bottom-left':
        tga_header[17] = 32

    # Save TGA file
    with open(f'./tmp/test_{origin.lower()}.tga', 'wb') as f:
        f.write(tga_header)

# Create TGA files with different origins
create_tga_file('top-left')
create_tga_file('bottom-left')
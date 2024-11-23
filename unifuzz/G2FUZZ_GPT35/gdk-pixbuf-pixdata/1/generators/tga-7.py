import struct

# Function to create a TGA file with developer-defined extension
def create_tga_file():
    # TGA header
    tga_header = struct.pack('<BBBHHBHHHHB', 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0)
    
    # Developer-defined extension data
    developer_extension = b"Developer Extensions: TGA format allows for developer-defined extensions to enhance functionality."
    
    # Write TGA file
    with open('./tmp/developer_extension.tga', 'wb') as f:
        f.write(tga_header)
        f.write(developer_extension)

# Create TGA file with developer-defined extension
create_tga_file()
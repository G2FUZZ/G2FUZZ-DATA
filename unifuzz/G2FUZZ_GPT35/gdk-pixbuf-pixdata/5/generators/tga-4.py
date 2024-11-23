import struct

# Function to create a TGA file with metadata
def create_tga_file_with_metadata(file_path, width, height, author, timestamp):
    # Define TGA header
    tga_header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, width & 0xFF, (width >> 8) & 0xFF,
                            height & 0xFF, (height >> 8) & 0xFF, 24, 0])

    # Add metadata to the TGA file
    metadata = f"Author: {author}\nTimestamp: {timestamp}\n"
    
    with open(file_path, 'wb') as file:
        file.write(tga_header)
        file.write(metadata.encode())

# Generate a TGA file with metadata
create_tga_file_with_metadata('./tmp/metadata_example.tga', 800, 600, 'John Doe', '2022-01-01')
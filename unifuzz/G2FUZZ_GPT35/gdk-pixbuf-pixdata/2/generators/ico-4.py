import struct

def create_ico_with_metadata(metadata):
    # ICO header structure
    ico_header = struct.pack('<HHH', 0, 1, len(metadata))
    
    # ICO file data with metadata
    ico_data = ico_header + metadata.encode()
    
    # Save the ICO file to ./tmp/ directory
    with open('./tmp/metadata_icon.ico', 'wb') as file:
        file.write(ico_data)

# Metadata to be added to the ICO file
metadata = "Author: John Doe\nCreation Date: 2022-01-01\nVersion: 1.0"

create_ico_with_metadata(metadata)
from PIL import Image
import struct
import os

def create_tga_with_attributes(filename, width, height, metadata):
    # Ensure the tmp directory exists
    os.makedirs('./tmp/', exist_ok=True)
    filepath = f'./tmp/{filename}'
    
    # Create an image
    image = Image.new("RGB", (width, height), "white")
    # Save the image as TGA
    image.save(filepath, format='TGA')
    
    # Open the file again to append the attribute and footer
    with open(filepath, 'ab') as file:
        # Developer-defined attribute/metadata section
        # In this example, we're directly converting the metadata string to bytes.
        # This section can be adapted to include more structured data as needed.
        attribute_data = metadata.encode('utf-8')
        attribute_length = len(attribute_data)
        
        # Append the developer-defined attribute information
        file.write(attribute_data)
        
        # TGA 2.0 footer
        # The footer contains 4 parts:
        # 1. The extension area offset (4 bytes): Points to the start of the developer area. Here we calculate it as the file size minus the attribute length.
        # 2. The developer area offset (4 bytes): Where our custom attributes start. Here, it's the file size before appending the footer minus the attribute length.
        # 3. The signature "TRUEVISION-XFILE" (18 bytes)
        # 4. A final "." (1 byte) and a NULL byte (1 byte) to indicate the end of the file.
        file_size = file.tell()
        extension_area_offset = file_size - attribute_length
        developer_area_offset = file_size - attribute_length
        footer = struct.pack('<II18sBx', extension_area_offset, developer_area_offset, b"TRUEVISION-XFILE", 46)
        file.write(footer)

# Example usage
metadata = "Author: Jane Doe; Copyright 2023; All Rights Reserved."
create_tga_with_attributes('example.tga', 100, 100, metadata)
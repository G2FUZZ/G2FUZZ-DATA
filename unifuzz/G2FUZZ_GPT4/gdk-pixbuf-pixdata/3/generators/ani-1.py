import os

def create_ani_file(file_path):
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # ANI file header and default structure
    # This is a simplified representation and might not be fully functional
    # as creating ANI files programmatically requires following the specific
    # RIFF file format structure for cursors, which is non-trivial and typically
    # not done manually in raw Python without a library.
    ani_header = b'RIFFxxxxACONanih36\x00\x00\x00\x24\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00LISTxxxxframicon\x00\x00\x00'
    frame_data = b''
    
    # Example: Creating two frames of simple binary data to simulate an animation
    # In a real scenario, this should be actual image data for the cursor frames
    for i in range(2):
        # Create dummy frame (should be real image data)
        frame = b'\x00\x01\x02\x03\x04\x05' * i  # Simplified example data
        frame_data += frame
    
    # Calculate and fill in the correct size for the RIFF and LIST chunks
    # This is a simplified example and might not directly apply to actual ani files
    file_size = len(ani_header) + len(frame_data) - 8  # RIFF chunk size
    list_size = len(frame_data) + 4  # LIST chunk size
    ani_header = ani_header.replace(b'xxxx', int.to_bytes(file_size, 4, 'little'))
    ani_header = ani_header.replace(b'xxxx', int.to_bytes(list_size, 4, 'little'), 1)

    ani_content = ani_header + frame_data
    
    # Write the ANI file
    with open(file_path, 'wb') as f:
        f.write(ani_content)

# Path where the ANI file will be saved
ani_file_path = './tmp/animated_cursor.ani'

# Create the ANI file
create_ani_file(ani_file_path)

print(f"ANI file saved to {ani_file_path}")
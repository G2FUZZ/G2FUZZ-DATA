import struct

# Create a simple ICO file with specified features
def create_ico_file():
    # ICO file header
    ico_header = struct.pack('<HHHBBB', 0, 1, 1, 1, 0, 0)
    
    # ICO file directory entry
    ico_entry = struct.pack('<BBBBHHII', 16, 16, 0, 0, 1, 0, 0, 0)
    
    # Combine header and directory entry
    ico_data = ico_header + ico_entry
    
    # Save the ICO file
    with open('./tmp/scalable_icon.ico', 'wb') as f:
        f.write(ico_data)

# Generate the ICO file
create_ico_file()
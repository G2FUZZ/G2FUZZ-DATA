import os
import struct

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Path to the .coff file
file_path = './tmp/example.coff'

# Simulating some optional header values (for demonstration purposes only)
entry_point_address = 0x1000
stack_size = 0x100000
heap_size = 0x100000

# Open the file in binary write mode
with open(file_path, 'wb') as coff_file:
    # Writing a mock optional header to the .coff file
    # This is a simplification and does not adhere to the actual COFF format
    # Format: I = unsigned int (4 bytes each)
    # Writing entry point address, stack size, and heap size
    coff_file.write(struct.pack('III', entry_point_address, stack_size, heap_size))

print(f'Mock COFF file with optional header created at: {file_path}')
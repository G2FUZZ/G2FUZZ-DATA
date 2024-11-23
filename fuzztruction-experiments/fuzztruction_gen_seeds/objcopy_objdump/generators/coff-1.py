import os
import struct

def create_coff_file(file_path):
    # Ensure the target directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # COFF File Header Fields (placeholders for this example)
    machine = 0x14C  # Machine type (x86)
    numberOfSections = 1  # Number of sections
    timeDateStamp = 0  # Time & date stamp
    pointerToSymbolTable = 0  # Pointer to symbol table (deprecated)
    numberOfSymbols = 0  # Number of symbols (deprecated)
    sizeOfOptionalHeader = 0  # Size of optional header
    characteristics = 0x102  # Characteristics (e.g., executable image)
    
    # Packing the header into bytes
    coff_header = struct.pack('<HHIIIHH', machine, numberOfSections, timeDateStamp,
                              pointerToSymbolTable, numberOfSymbols, sizeOfOptionalHeader, characteristics)
    
    # Writing the header to the file
    with open(file_path, 'wb') as f:
        f.write(coff_header)
        
    print(f'COFF file created at: {file_path}')

# Specify the path for the new COFF file
coff_file_path = './tmp/sample.coff'

# Create the COFF file
create_coff_file(coff_file_path)
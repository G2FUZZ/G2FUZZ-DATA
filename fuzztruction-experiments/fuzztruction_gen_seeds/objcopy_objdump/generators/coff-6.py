import os
import struct

def create_coff_file(file_path, is_big_endian):
    # COFF file header structure (simplified):
    #   - Machine (2 bytes)
    #   - Number of Sections (2 bytes)
    #   - Time Date Stamp (4 bytes)
    #   - Pointer to Symbol Table (4 bytes)
    #   - Number of Symbols (4 bytes)
    #   - Size of Optional Header (2 bytes)
    #   - Characteristics (2 bytes)
    
    # Choose endian format
    endian_format = '>' if is_big_endian else '<'  # '>' for big-endian, '<' for little-endian
    
    # Example values for a minimal COFF header (adjust according to actual needs)
    machine_type = 0x14C  # Example: 0x14C for x86
    num_of_sections = 0
    time_date_stamp = 0
    ptr_to_sym_tab = 0
    num_of_symbols = 0
    size_of_opt_header = 0
    characteristics = 0x102  # Example: Relocatable, Executable, Line nums stripped, 32 bit machine
    
    # Pack the header into binary format
    header_format = f'{endian_format}HHLLLHH'
    header_data = struct.pack(header_format, machine_type, num_of_sections, time_date_stamp,
                              ptr_to_sym_tab, num_of_symbols, size_of_opt_header, characteristics)
    
    # Ensure the `./tmp/` directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the binary data to the COFF file
    with open(file_path, 'wb') as f:
        f.write(header_data)

# Example usage
create_coff_file('./tmp/example_coff_little_endian.coff', is_big_endian=False)
create_coff_file('./tmp/example_coff_big_endian.coff', is_big_endian=True)
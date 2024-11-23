import os
from struct import pack

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a simple COFF file with relocation information
def create_coff_with_relocation(filename):
    # COFF Header
    # For simplicity, many fields will be set to zero or simple values, as this example
    # is not focusing on creating a fully functional COFF file but to demonstrate the inclusion
    # of relocation information.
    header = pack(
        '<HHLLLHH',
        0x14C,  # Machine type (x86)
        1,      # Number of sections
        0,      # TimeDateStamp
        0,      # PointerToSymbolTable (set later)
        0,      # NumberOfSymbols (set later)
        0x20,   # SizeOfOptionalHeader
        0       # Characteristics
    )

    # Section Header
    section_header = pack(
        '<8sLLLLLLHHI',
        b'.data\0\0',  # Name
        0,             # VirtualSize
        0,             # VirtualAddress
        8,             # SizeOfRawData
        0x80,          # PointerToRawData (set after headers)
        0x80 + 8,      # PointerToRelocations
        0,             # PointerToLinenumbers
        1,             # NumberOfRelocations
        0,             # NumberOfLinenumbers
        0x40           # Characteristics (contains initialized data)
    )

    # Relocation entry
    # This part simulates the relocation information.
    relocation_entry = pack(
        '<LLH',
        0,      # VirtualAddress
        0,      # SymbolTableIndex
        0x14    # Type
    )

    # Simulated data section
    # In a real COFF file, this would be the compiled code or data.
    data_section = b'\x00' * 8

    # Combine all parts
    coff_file_content = header + section_header + data_section + relocation_entry

    # Write the COFF file
    with open(filename, 'wb') as f:
        f.write(coff_file_content)

# Create a COFF file with relocation information
create_coff_with_relocation('./tmp/sample.coff')
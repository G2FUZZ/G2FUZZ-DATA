import os

def create_elf_with_pht(output_path):
    # ELF Header
    elf_header = bytes([
        0x7f, 0x45, 0x4c, 0x46, # Magic number
        0x01, # 32-bit
        0x01, # Little endian
        0x01, # ELF version
        0x00, # Target ABI
        0x00, # ABI version
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # Padding
        0x02, 0x00, # Type: EXEC (Executable file)
        0x03, 0x00, # Machine: x86
        0x01, 0x00, 0x00, 0x00, # Version
        0x54, 0x00, 0x00, 0x00, # Entry point address
        0x34, 0x00, 0x00, 0x00, # Start of program headers
        0x00, 0x00, 0x00, 0x00, # Start of section headers
        0x00, 0x00, 0x00, 0x00, # Flags
        0x34, 0x00, # ELF header size
        0x20, 0x00, # Size of program header entry
        0x01, 0x00, # Number of program header entries
        0x00, 0x00, # Size of section header entry
        0x00, 0x00, # Number of section header entries
        0x00, 0x00, # Section header string table index
    ])

    # Program Header Table
    pht = bytes([
        0x01, 0x00, 0x00, 0x00, # Type: LOAD
        0x00, 0x00, 0x00, 0x00, # Offset
        0x54, 0x00, 0x00, 0x00, # Virtual address
        0x54, 0x00, 0x00, 0x00, # Physical address (unused)
        0x00, 0x00, 0x00, 0x00, # File size
        0x00, 0x00, 0x00, 0x00, # Memory size
        0x05, 0x00, 0x00, 0x00, # Flags
        0x00, 0x00, 0x00, 0x00, # Align
    ])

    # Combine ELF header and PHT
    elf_file = elf_header + pht

    # Write to file
    with open(output_path, 'wb') as f:
        f.write(elf_file)

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create the ELF file
create_elf_with_pht('./tmp/simple_elf_with_pht.elf')
import os

def create_elf_file(filename):
    # ELF Header for a 64-bit executable
    # This is a minimal and static ELF header; many fields are set to zero
    elf_header = bytes([
        0x7f, 0x45, 0x4c, 0x46,  # Magic number
        0x02,  # 64-bit architecture
        0x01,  # Little endian
        0x01,  # ELF header version
        0x00,  # OS ABI (UNIX System V ABI)
        0x00,  # ABI version
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Padding
        0x02, 0x00,  # Type: EXEC (Executable file)
        0x3e, 0x00,  # Machine: x86-64
        0x01, 0x00, 0x00, 0x00,  # Version
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Entry point address
        0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Program header table file offset
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Section header table file offset
        0x00, 0x00, 0x00, 0x00,  # Flags
        0x40, 0x00,  # ELF header size
        0x00, 0x00,  # Program header table entry size
        0x00, 0x00,  # Program header table entry count
        0x00, 0x00,  # Section header table entry size
        0x00, 0x00,  # Section header table entry count
        0x00, 0x00,  # Section header string table index
    ])

    # Ensure the ./tmp/ directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Write the ELF header to the file
    with open(filename, 'wb') as f:
        f.write(elf_header)

# Replace 'your_file.elf' with the desired file name
create_elf_file('./tmp/your_file.elf')
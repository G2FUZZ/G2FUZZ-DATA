import os

def create_elf_with_relocation():
    # ELF Header
    elf_header = bytes([
        0x7f, 0x45, 0x4c, 0x46,  # Magic number
        0x01,  # 32-bit
        0x01,  # Little endian
        0x01,  # ELF version
        0x00,  # Target ABI
        0x00,  # ABI Version
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Padding
        0x02, 0x00,  # Type: EXEC (Executable file)
        0x03, 0x00,  # Machine: x86
        0x01, 0x00, 0x00, 0x00,  # Version
        0x54, 0x80, 0x04, 0x08,  # Entry point address
        0x34, 0x00, 0x00, 0x00,  # Start of program headers
        0x00, 0x00, 0x00, 0x00,  # Start of section headers
        0x00, 0x00, 0x00, 0x00,  # Flags
        0x34, 0x00,  # Size of this header
        0x20, 0x00,  # Size of program headers
        0x01, 0x00,  # Number of program headers
        0x00, 0x00,  # Size of section headers
        0x00, 0x00,  # Number of section headers
        0x00, 0x00   # Section header string table index
    ])

    # Program Header
    program_header = bytes([
        0x01, 0x00, 0x00, 0x00,  # Type: LOAD
        0x54, 0x80, 0x04, 0x08,  # Offset
        0x54, 0x80, 0x04, 0x08,  # Virtual address
        0x54, 0x80, 0x04, 0x08,  # Physical address
        0x05, 0x00, 0x00, 0x00,  # File size
        0x05, 0x00, 0x00, 0x00,  # Memory size
        0x05, 0x00, 0x00, 0x00,  # Flags
        0x00, 0x10, 0x00, 0x00   # Align
    ])

    # Relocation Entry Section
    # Normally, relocation entries would be more complex and specific to the use case.
    # This is a simplified, illustrative example.
    relocation_section = bytes([
        0x00, 0x00, 0x00, 0x00,  # Offset
        0x00, 0x00, 0x00, 0x00   # Info
    ])

    # Combine all parts
    elf_file_content = elf_header + program_header + relocation_section

    # Ensure the tmp directory exists
    os.makedirs('./tmp', exist_ok=True)

    # Write the ELF file
    with open('./tmp/example_relocation.elf', 'wb') as elf_file:
        elf_file.write(elf_file_content)

if __name__ == '__main__':
    create_elf_with_relocation()
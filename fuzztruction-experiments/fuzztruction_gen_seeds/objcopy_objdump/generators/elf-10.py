def create_elf_with_custom_section():
    # ELF Header
    elf_header = bytes([
        0x7f, 0x45, 0x4c, 0x46,  # Magic Number
        0x01,                     # 32-bit
        0x01,                     # Little endian
        0x01,                     # ELF version 1
        0x00,                     # Target ABI
        0x00,                     # ABI Version
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Padding
        0x02, 0x00,               # Type: EXEC (Executable)
        0x03, 0x00,               # Machine: x86
        0x01, 0x00, 0x00, 0x00,  # Version
        0x54, 0x80, 0x04, 0x08,  # Entry point address
        0x34, 0x00, 0x00, 0x00,  # Start of program headers
        0x00, 0x00, 0x00, 0x00,  # Start of section headers
        0x00, 0x00, 0x00, 0x00,  # Flags
        0x34, 0x00,               # Size of this header
        0x20, 0x00,               # Size of program headers
        0x01, 0x00,               # Number of program headers
        0x00, 0x00,               # Size of section headers
        0x00, 0x00,               # Number of section headers
        0x00, 0x00                # Section header string table index
    ])

    # Custom Section
    custom_section = b'\x00' * 16  # Placeholder for custom section content

    # Combine ELF header and custom section
    elf_file_content = elf_header + custom_section

    # Write to file
    with open('./tmp/custom_elf', 'wb') as file:
        file.write(elf_file_content)

if __name__ == '__main__':
    create_elf_with_custom_section()
import os

# Basic ELF header structure for a 64-bit executable
elf_header = bytes([
    0x7f, 0x45, 0x4c, 0x46,  # Magic number
    0x02,                    # 64-bit architecture
    0x01,                    # Little endian
    0x01,                    # ELF version
    0x00,                    # OS ABI (UNIX - System V)
    0x00,                    # ABI version
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Padding
    0x02, 0x00,              # Type: EXEC (Executable file)
    0x3e, 0x00,              # Machine: x86-64
    0x01, 0x00, 0x00, 0x00,  # Version
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Entry point address
    0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Program header table file offset
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Section header table file offset
    0x00, 0x00, 0x00, 0x00,  # Flags
    0x40, 0x00,              # ELF header size
    0x00, 0x00,              # Program header table entry size
    0x00, 0x00,              # Program header table entry count
    0x00, 0x00,              # Section header table entry size
    0x00, 0x00,              # Section header table entry count
    0x00, 0x00               # Section header string table index
])

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Write the ELF header to a file
with open('./tmp/sample.elf', 'wb') as elf_file:
    elf_file.write(elf_header)

print("ELF file created at ./tmp/sample.elf")
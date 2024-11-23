import struct
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_simple_elf_file(filename):
    with open(filename, 'wb') as f:
        # ELF Header
        # This is a very simplified example and does not include all necessary fields
        # and settings for a valid ELF file.
        e_ident = b'\x7fELF'  # ELF Magic number
        e_ident += b'\x02'  # 64-bit
        e_ident += b'\x01'  # Little endian
        e_ident += b'\x01'  # ELF version
        e_ident += b'\x00' * 8  # Padding
        e_type = struct.pack('<H', 2)  # ET_EXEC (Executable file)
        e_machine = struct.pack('<H', 62)  # EM_X86_64 (AMD x86-64 architecture)
        e_version = struct.pack('<I', 1)  # Version 1
        e_entry = struct.pack('<Q', 0x400080)  # Entry point address
        e_phoff = struct.pack('<Q', 0x40)  # Start of program headers
        e_shoff = struct.pack('<Q', 0)  # Start of section headers (placeholder)
        e_flags = struct.pack('<I', 0)  # Flags
        e_ehsize = struct.pack('<H', 64)  # ELF header size
        e_phentsize = struct.pack('<H', 56)  # Program header table entry size
        e_phnum = struct.pack('<H', 1)  # Number of program headers
        e_shentsize = struct.pack('<H', 64)  # Section header table entry size
        e_shnum = struct.pack('<H', 3)  # Number of section headers
        e_shstrndx = struct.pack('<H', 2)  # Section header string table index

        # Write the ELF header
        f.write(e_ident + e_type + e_machine + e_version + e_entry + e_phoff +
                e_shoff + e_flags + e_ehsize + e_phentsize + e_phnum +
                e_shentsize + e_shnum + e_shstrndx)

        # Additional code would be needed here to create and write program headers,
        # section headers, and section data.

# Create and save an ELF file with the specified features
create_simple_elf_file('./tmp/example.elf')
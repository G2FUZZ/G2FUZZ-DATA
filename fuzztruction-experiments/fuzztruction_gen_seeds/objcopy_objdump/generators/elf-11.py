import os

def create_elf_file(filename, bitness, endianness):
    # ELF Magic Number and Class
    elf_magic_number = b"\x7fELF"
    elf_class = b"\x01" if bitness == 32 else b"\x02"
    
    # Endianness
    elf_data = b"\x01" if endianness == "little" else b"\x02"
    
    # ELF Header
    if bitness == 32:
        # 32-bit ELF Header is 52 bytes: ELF magic number (4) + class (1) + data (1) + version (1) + padding (9) + e_type (2) + e_machine (2) + e_version (4) + e_entry (4) + e_phoff (4) + e_shoff (4) + e_flags (4) + e_ehsize (2) + e_phentsize (2) + e_phnum (2) + e_shentsize (2) + e_shnum (2) + e_shstrndx (2)
        elf_header = elf_magic_number + elf_class + elf_data + b"\x01" + (b"\x00" * 9) + (b"\x00" * (52 - 16))
    else:  # 64-bit
        # 64-bit ELF Header is 64 bytes: ELF magic number (4) + class (1) + data (1) + version (1) + padding (9) + e_type (2) + e_machine (2) + e_version (4) + e_entry (8) + e_phoff (8) + e_shoff (8) + e_flags (4) + e_ehsize (2) + e_phentsize (2) + e_phnum (2) + e_shentsize (2) + e_shnum (2) + e_shstrndx (2)
        elf_header = elf_magic_number + elf_class + elf_data + b"\x01" + (b"\x00" * 9) + (b"\x00" * (64 - 16))
    
    # Write the ELF header to a file
    os.makedirs("./tmp", exist_ok=True)
    with open(f"./tmp/{filename}", "wb") as f:
        f.write(elf_header)

# Create a 32-bit little-endian ELF file
create_elf_file("elf_32_little_endian", 32, "little")

# Create a 64-bit big-endian ELF file
create_elf_file("elf_64_big_endian", 64, "big")
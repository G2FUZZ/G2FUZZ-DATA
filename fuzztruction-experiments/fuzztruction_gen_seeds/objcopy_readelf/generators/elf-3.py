import os

def create_elf_with_section_header_table():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    elf_path = './tmp/sample.elf'

    # ELF Header
    e_ident = b'\x7fELF\x01\x01\x01\x00' + b'\x00'*8  # ELF Magic number, 32-bit, little endian, version 1
    e_type = b'\x01\x00'  # Type: REL (Relocatable file)
    e_machine = b'\x03\x00'  # Machine: Intel 80386
    e_version = b'\x01\x00\x00\x00'  # Version: 1
    e_entry = b'\x00\x00\x00\x00'  # Entry point address
    e_phoff = b'\x00\x00\x00\x00'  # Program header table file offset
    e_shoff = b'\x34\x00\x00\x00'  # Section header table file offset, placing it after the header
    e_flags = b'\x00\x00\x00\x00'  # Processor-specific flags
    e_ehsize = b'\x34\x00'  # ELF header size
    e_phentsize = b'\x00\x00'  # Program header table entry size
    e_phnum = b'\x00\x00'  # Program header table entry count
    e_shentsize = b'\x28\x00'  # Section header table entry size
    e_shnum = b'\x02\x00'  # Section header table entry count
    e_shstrndx = b'\x01\x00'  # Section header string table index

    # Assemble the ELF header
    elf_header = e_ident + e_type + e_machine + e_version + e_entry + e_phoff + e_shoff + e_flags + e_ehsize + e_phentsize + e_phnum + e_shentsize + e_shnum + e_shstrndx

    # Section Headers
    sh_null = b'\x00'*40  # Null section header
    # Section header for the section header string table (name, type, flags, addr, offset, size, link, info, addralign, entsize)
    sh_strtab = b'\x01\x00\x00\x00' + b'\x03\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x54\x00\x00\x00' + b'\x11\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00' + b'\x01\x00\x00\x00' + b'\x00\x00\x00\x00'
    # Section names for the section header string table, includes null, .shstrtab
    sh_strtab_data = b'\x00.shstrtab\x00'

    # Assemble the ELF file
    with open(elf_path, 'wb') as elf_file:
        elf_file.write(elf_header)
        elf_file.write(sh_null)
        elf_file.write(sh_strtab)
        elf_file.seek(int.from_bytes(e_shoff, 'little') + int.from_bytes(e_shentsize, 'little')*int.from_bytes(e_shnum, 'little'))
        elf_file.write(sh_strtab_data)

    print(f"ELF file created at: {elf_path}")

create_elf_with_section_header_table()
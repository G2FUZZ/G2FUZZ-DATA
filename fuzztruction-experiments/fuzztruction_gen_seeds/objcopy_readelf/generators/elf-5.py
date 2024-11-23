import os
from elftools.elf.elffile import ELFFile
from io import BytesIO

def create_elf_with_symbol_table():
    # Create a temporary directory if it doesn't exist
    tmp_dir = './tmp/'
    os.makedirs(tmp_dir, exist_ok=True)
    elf_file_path = os.path.join(tmp_dir, 'sample_elf_with_symbol_table.elf')

    # Creating an ELF header
    e_ident = b'\x7fELF\x01\x01\x01\x00' + b'\x00'*8  # ELF header for 32-bit, little endian
    e_type = 1  # ET_REL (Relocatable file)
    e_machine = 3  # EM_386 (Intel 80386)
    e_version = 1
    e_entry = 0
    e_phoff = 0
    e_shoff = 52  # Assuming start of section header right after headers
    e_flags = 0
    e_ehsize = 52  # ELF header size
    e_phentsize = 0
    e_phnum = 0
    e_shentsize = 40  # Section header size
    e_shnum = 3  # Number of section headers
    e_shstrndx = 1  # Section header string table index

    elf_header = (e_ident +
                  e_type.to_bytes(2, byteorder='little') +
                  e_machine.to_bytes(2, byteorder='little') +
                  e_version.to_bytes(4, byteorder='little') +
                  e_entry.to_bytes(4, byteorder='little') +
                  e_phoff.to_bytes(4, byteorder='little') +
                  e_shoff.to_bytes(4, byteorder='little') +
                  e_flags.to_bytes(4, byteorder='little') +
                  e_ehsize.to_bytes(2, byteorder='little') +
                  e_phentsize.to_bytes(2, byteorder='little') +
                  e_phnum.to_bytes(2, byteorder='little') +
                  e_shentsize.to_bytes(2, byteorder='little') +
                  e_shnum.to_bytes(2, byteorder='little') +
                  e_shstrndx.to_bytes(2, byteorder='little'))

    # Note: The following sections are placeholders and do not represent a valid ELF file structure.
    # Proper section headers and symbol table entries would need to be created here.
    shstrtab_section = b'\x00.shstrtab\x00.symtab\x00.strtab\x00'
    symtab_section = b''  # Placeholder for symbol table entries
    strtab_section = b'\x00main\x00variable\x00'

    # Writing the ELF file
    with open(elf_file_path, 'wb') as elf_file:
        elf_file.write(elf_header)
        # Note: Proper offsets and sizes for each section would need to be calculated and written here.
        elf_file.write(shstrtab_section)
        elf_file.write(symtab_section)
        elf_file.write(strtab_section)

    # Attempting to read the ELF file (this may still fail if the file is not fully compliant)
    try:
        with open(elf_file_path, 'rb') as elf_file:
            elf = ELFFile(elf_file)
            print(f"ELF header: {elf.header}")
            for section in elf.iter_sections():
                print(f"Section: {section.name}")
    except Exception as e:
        print(f"Error reading ELF file: {e}")

if __name__ == '__main__':
    create_elf_with_symbol_table()
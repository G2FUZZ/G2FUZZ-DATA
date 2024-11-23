# Removed the incorrect import statement
from elftools.elf.elffile import ELFFile
from elftools.elf.enums import ENUM_E_MACHINE
import io

# Function to create an ELF header
def create_elf_header():
    # Define a simple ELF header using construct
    e_ident = b"\x7fELF"  # ELF Magic number
    e_type = b"\x02\x00"  # ET_EXEC (Executable file)
    e_machine = b"\x3E\x00"  # EM_X86_64 (AMD x86-64 architecture)
    e_version = b"\x01\x00\x00\x00"  # EV_CURRENT
    e_entry = b"\x00\x00\x00\x00\x00\x00\x00\x00"  # Entry point address
    e_phoff = b"\x40\x00\x00\x00\x00\x00\x00\x00"  # Program header table file offset
    e_shoff = b"\x00\x00\x00\x00\x00\x00\x00\x00"  # Section header table file offset
    e_flags = b"\x00\x00\x00\x00"  # Processor-specific flags
    e_ehsize = b"\x40\x00"  # ELF header size
    e_phentsize = b"\x00\x00"  # Program header table entry size
    e_phnum = b"\x00\x00"  # Program header table entry count
    e_shentsize = b"\x00\x00"  # Section header table entry size
    e_shnum = b"\x00\x00"  # Section header table entry count
    e_shstrndx = b"\x00\x00"  # Section header string table index

    # Combine all parts into the final ELF header
    elf_header = (
        e_ident + e_type + e_machine + e_version +
        e_entry + e_phoff + e_shoff + e_flags +
        e_ehsize + e_phentsize + e_phnum +
        e_shentsize + e_shnum + e_shstrndx
    )

    return elf_header

# Main function to generate the ELF file
def generate_elf_file(filepath):
    elf_header = create_elf_header()
    with open(filepath, "wb") as elf_file:
        elf_file.write(elf_header)

# Directory and file name
filename = "./tmp/simple_elf_file.elf"
generate_elf_file(filename)
print(f"ELF file created at {filename}")
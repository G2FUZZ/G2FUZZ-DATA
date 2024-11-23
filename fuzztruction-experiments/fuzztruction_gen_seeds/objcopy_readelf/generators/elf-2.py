import os
import struct

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_elf_64bit(filename):
    # ELF Header for a 64-bit executable
    e_ident = b'\x7fELF'  # ELF Magic Number
    e_ident += b'\x02'    # EI_CLASS (64-bit)
    e_ident += b'\x01'    # EI_DATA (Little-endian)
    e_ident += b'\x01'    # EI_VERSION (Current version)
    e_ident += b'\x00'    # EI_OSABI (System V)
    e_ident += b'\x00'    # EI_ABIVERSION
    e_ident += b'\x00'*7  # EI_PAD (Padding)
    
    e_type = struct.pack('<H', 2)               # ET_EXEC (Executable file)
    e_machine = struct.pack('<H', 0x3E)         # EM_X86_64 (AMD x86-64 architecture)
    e_version = struct.pack('<I', 1)            # EV_CURRENT
    e_entry = struct.pack('<Q', 0x400000)       # Entry point address
    e_phoff = struct.pack('<Q', 0x40)           # Program header table file offset
    e_shoff = struct.pack('<Q', 0)              # Section header table file offset
    e_flags = struct.pack('<I', 0)              # Processor-specific flags
    e_ehsize = struct.pack('<H', 0x40)          # ELF header size
    e_phentsize = struct.pack('<H', 0x38)       # Program header table entry size
    e_phnum = struct.pack('<H', 1)              # Number of program header entries
    e_shentsize = struct.pack('<H', 0)          # Section header table entry size
    e_shnum = struct.pack('<H', 0)              # Number of section header entries
    e_shstrndx = struct.pack('<H', 0)           # Section header string table index
    
    # Construct the ELF header
    elf_header = (e_ident + e_type + e_machine + e_version + e_entry + e_phoff +
                  e_shoff + e_flags + e_ehsize + e_phentsize + e_phnum +
                  e_shentsize + e_shnum + e_shstrndx)
    
    # Program Header (Just a placeholder, not a valid one)
    p_type = struct.pack('<I', 1)               # PT_LOAD (Loadable segment)
    p_flags = struct.pack('<I', 5)              # Read and Execute
    p_offset = struct.pack('<Q', 0x1000)        # Offset in the file
    p_vaddr = struct.pack('<Q', 0x400000)       # Virtual address in memory
    p_paddr = struct.pack('<Q', 0x400000)       # Physical address (unused)
    p_filesz = struct.pack('<Q', 0x1000)        # Size of the segment in the file
    p_memsz = struct.pack('<Q', 0x1000)         # Size of the segment in memory
    p_align = struct.pack('<Q', 0x1000)         # Alignment
    
    # Construct the program header
    program_header = p_type + p_flags + p_offset + p_vaddr + p_paddr + p_filesz + p_memsz + p_align
    
    with open(filename, 'wb') as f:
        f.write(elf_header)
        f.write(program_header)
        # Adding a simple placeholder for the segment content
        f.seek(0x1000 - 1)
        f.write(b'\x00')

create_elf_64bit('./tmp/sample_elf_64bit')
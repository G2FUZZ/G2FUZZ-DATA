import os

def create_elf_with_phdr():
    # Ensure the tmp directory exists
    os.makedirs("./tmp", exist_ok=True)
    
    # Path to the ELF file to be created
    elf_path = "./tmp/example.elf"
    
    # ELF Header
    e_ident = b"\x7fELF" + b"\x01\x01\x01" + b"\x00" * 9  # ELF Magic Number + Class (32-bit) + Data (little-endian) + Version + Padding
    e_type = b"\x02\x00"  # Type: EXEC (Executable file)
    e_machine = b"\x03\x00"  # Machine: Intel 80386
    e_version = b"\x01\x00\x00\x00"  # Version: 1
    e_entry = b"\x54\x80\x04\x08"  # Entry point address: 0x08048054
    e_phoff = b"\x34\x00\x00\x00"  # Start of program headers: 52 bytes into the file
    e_shoff = b"\x00\x00\x00\x00"  # Start of section headers: 0 (no section headers in this example)
    e_flags = b"\x00\x00\x00\x00"  # Flags: 0
    e_ehsize = b"\x34\x00"  # ELF header size in bytes: 52
    e_phentsize = b"\x20\x00"  # Size of one program header table entry: 32
    e_phnum = b"\x01\x00"  # Number of program header table entries: 1
    e_shentsize = b"\x00\x00"  # Size of a section header table entry: 0
    e_shnum = b"\x00\x00"  # Number of section header table entries: 0
    e_shstrndx = b"\x00\x00"  # Section header string table index: 0

    elf_header = e_ident + e_type + e_machine + e_version + e_entry + e_phoff + e_shoff + e_flags + e_ehsize + e_phentsize + e_phnum + e_shentsize + e_shnum + e_shstrndx
    
    # Program Header Table
    p_type = b"\x01\x00\x00\x00"  # Type: PT_LOAD (Loadable segment)
    p_offset = b"\x00\x00\x00\x00"  # Offset: 0
    p_vaddr = b"\x54\x80\x04\x08"  # Virtual address: 0x08048054
    p_paddr = b"\x54\x80\x04\x08"  # Physical address: 0x08048054 (In many cases, virtual and physical addresses are the same)
    p_filesz = b"\x00\x00\x00\x00"  # Size of segment in file: 0 (for demonstration)
    p_memsz = b"\x00\x00\x00\x00"  # Size of segment in memory: 0 (for demonstration)
    p_flags = b"\x05\x00\x00\x00"  # Flags: Read, Execute
    p_align = b"\x00\x10\x00\x00"  # Alignment: 16

    program_header = p_type + p_offset + p_vaddr + p_paddr + p_filesz + p_memsz + p_flags + p_align
    
    with open(elf_path, "wb") as elf_file:
        elf_file.write(elf_header + program_header)
    
    print(f"ELF file with Program Header created at: {elf_path}")

create_elf_with_phdr()
from elftools.elf.elffile import ELFFile
from elftools.elf.enums import ENUM_E_MACHINE
from keystone import Ks, KS_ARCH_X86, KS_MODE_32, KS_ARCH_ARM, KS_MODE_ARM, KS_ARCH_MIPS, KS_MODE_MIPS32
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define a simple assembly instruction for each architecture
code_to_assemble = {
    'x86': 'nop',
    'arm': 'nop',
    'mips': 'nop'
}

# Define the architecture settings for Keystone assembler
arch_settings = {
    'x86': (KS_ARCH_X86, KS_MODE_32),
    'arm': (KS_ARCH_ARM, KS_MODE_ARM),
    'mips': (KS_ARCH_MIPS, KS_MODE_MIPS32),
}

# Function to create an ELF file
def create_elf_file(arch, machine, assembled_code):
    with open(f'./tmp/sample_{arch}.elf', 'wb') as f:
        # ELF header placeholder, this is a minimal and not fully correct example, 
        # real ELF file creation would require setting up all necessary headers and sections
        f.write(b'\x7fELF')  # Magic number
        if arch == 'x86':
            f.write(b'\x01')  # 32-bit
        elif arch in ['arm', 'mips']:
            f.write(b'\x02')  # 64-bit for simplicity
        f.write(b'\x01')  # Little endian
        f.write(b'\x01')  # ELF version
        f.write(b'\x00') * 8  # Padding
        f.write(machine.to_bytes(2, 'little'))  # Machine type
        f.write(b'\x01\x00')  # Type: REL (Relocatable file)
        f.write(b'\x00' * 32)  # Padding to simulate e_entry and program header start, not actually functional
        # Write the assembled code directly, in a real scenario this should be placed in a proper section
        f.write(assembled_code)

# Assemble and create ELF files for each architecture
for arch, settings in arch_settings.items():
    ks = Ks(*settings)
    encoding, _ = ks.asm(code_to_assemble[arch])
    assembled_code = bytes(encoding)
    
    if arch == 'x86':
        machine = ENUM_E_MACHINE['EM_386']
    elif arch == 'arm':
        machine = ENUM_E_MACHINE['EM_ARM']
    elif arch == 'mips':
        machine = ENUM_E_MACHINE['EM_MIPS']
    
    create_elf_file(arch, machine, assembled_code)

print("ELF files generated in ./tmp/")
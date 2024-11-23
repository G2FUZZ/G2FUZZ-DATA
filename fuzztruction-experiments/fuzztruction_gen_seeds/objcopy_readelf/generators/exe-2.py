import pefile
import os

# Create the directories if they do not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the template for a minimal PE file
pe_template = (
    b"MZ"                                  # e_magic
    + b"\x90\x00"                          # e_cblp
    + b"\x03\x00"                          # e_cp
    + b"\x00\x00"                          # e_crlc
    + b"\x04\x00"                          # e_cparhdr
    + b"\x00\x00"                          # e_minalloc
    + b"\xff\xff"                          # e_maxalloc
    + b"\x00\x00"                          # e_ss
    + b"\xb8\x00"                          # e_sp
    + b"\x00\x00"                          # e_csum
    + b"\x00\x00"                          # e_ip
    + b"\x00\x00"                          # e_cs
    + b"\x40\x00"                          # e_lfarlc
    + b"\x00\x00"                          # e_ovno
    + b"\x00\x00\x00\x00\x00\x00\x00\x00"  # e_res
    + b"\x00\x00"                          # e_oemid
    + b"\x00\x00"                          # e_oeminfo
    + b"\x00\x00\x00\x00\x00\x00\x00\x00"  # e_res2
    + b"\x00\x00\x00\x00"                  # e_lfanew
    + b"PE\x00\x00"                        # Signature
    + b"L\x01\x04\x00"                     # Machine, NumberOfSections
    + b"\x00\x00\x00\x00"                  # TimeDateStamp
    + b"\x00\x00\x00\x00"                  # PointerToSymbolTable
    + b"\x00\x00\x00\x00"                  # NumberOfSymbols
    + b"\xE0\x00\x00\x00"                  # SizeOfOptionalHeader
    + b"\x02\x01\x00\x00"                  # Characteristics
    + b"\x0b\x02\x00\x00"                  # Magic, MajorLinkerVersion
    + b"\x00\x00\x00\x00" * 15             # Padding to simulate headers
    + b"\x2e\x74\x65\x78\x74\x00\x00\x00"  # .text
    + b"\x00\x10\x00\x00\x00\x10\x00\x00"
    + b"\x00\x02\x00\x00\x00\x02\x00\x00"
    + b"\x00\x00\x00\x00\x20\x00\x50\x60"
    + b"\x2e\x64\x61\x74\x61\x00\x00\x00"  # .data
    + b"\x00\x10\x00\x00\x00\x20\x00\x00"
    + b"\x00\x02\x00\x00\x00\x04\x00\x00"
    + b"\x00\x00\x00\x00\x40\x00\x40\xC0"
    + b"\x2e\x62\x73\x73\x00\x00\x00\x00"  # .bss
    + b"\x00\x10\x00\x00\x00\x30\x00\x00"
    + b"\x00\x02\x00\x00\x00\x06\x00\x00"
    + b"\x00\x00\x00\x00\x80\x00\xC0\xC0"
    + b"\x00" * 512                         # Padding to make a valid file size
)

# Save the PE file
file_path = './tmp/example_pe_file.exe'
with open(file_path, 'wb') as f:
    f.write(pe_template)

print("PE file generated and saved to:", file_path)
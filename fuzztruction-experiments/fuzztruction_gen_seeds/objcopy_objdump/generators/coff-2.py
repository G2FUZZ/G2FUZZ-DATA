import os
import struct

def create_coff_file(filename):
    # Ensure the tmp directory exists
    os.makedirs("./tmp", exist_ok=True)
    filepath = os.path.join("./tmp", filename)

    # Open file in binary write mode
    with open(filepath, "wb") as f:
        # COFF File Header (simplified)
        # Just for demonstration, not accurate for real COFF structure
        f.write(struct.pack('<H', 0x014C))  # Machine (Intel 386)
        f.write(struct.pack('<H', 1))       # Number of Sections
        f.write(struct.pack('<L', 0))       # Time Date Stamp
        f.write(struct.pack('<L', 0))       # Pointer to Symbol Table (unused here)
        f.write(struct.pack('<L', 0))       # Number of Symbols (unused here)
        f.write(struct.pack('<H', 0))       # Size of Optional Header (no optional header for simplicity)
        f.write(struct.pack('<H', 0))       # Characteristics

        # Section Header (simplified)
        # Again, simplified and not fully representative of a real COFF section header
        section_name = ".text".ljust(8, '\x00')  # Section name (padded to 8 bytes)
        f.write(section_name.encode('utf-8'))   # Name
        f.write(struct.pack('<L', 0x1000))      # Virtual Size
        f.write(struct.pack('<L', 0x1000))      # Virtual Address
        f.write(struct.pack('<L', 0x200))       # Size Of Raw Data
        f.write(struct.pack('<L', 0x200))       # Pointer To Raw Data
        f.write(struct.pack('<L', 0))           # Pointer To Relocations
        f.write(struct.pack('<L', 0))           # Pointer To Linenumbers
        f.write(struct.pack('<H', 0))           # Number Of Relocations
        f.write(struct.pack('<H', 0))           # Number Of Linenumbers
        f.write(struct.pack('<L', 0x60000020))  # Characteristics (code section)

    print(f"COFF file '{filename}' has been created in './tmp/' directory.")

# Replace 'example.coff' with your desired file name
create_coff_file("example.coff")
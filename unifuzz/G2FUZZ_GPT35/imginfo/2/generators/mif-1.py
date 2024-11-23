import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Generate MIF files
for i in range(3):
    with open(f'./tmp/file_{i}.mif', 'w') as file:
        file.write("""DEPTH = 256;
WIDTH = 8;
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT
BEGIN
""")
        for addr in range(256):
            data = (addr + i) % 256
            file.write(f"{addr:02X} : {data:02X};\n")
        
        file.write("END;\n")
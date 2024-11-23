import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Generate MIF files with interleaved data patterns
for i in range(3):
    with open(f'./tmp/file_{i}.mif', 'w') as file:
        file.write("""DEPTH = 512;
WIDTH = 16;
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT
BEGIN
""")
        for addr in range(256):
            data = (addr + i) % 256
            file.write(f"{addr:02X} : {data:02X}{(data+1)%256:02X};\n")
        
        file.write("256 : 00FF; 257 : FFFF;\n")  # Example of specific file structure
        
        for addr in range(258, 512):
            data = (addr - i) % 256
            file.write(f"{addr:02X} : {data:02X}{(data-1)%256:02X};\n")
        
        file.write("END;\n")
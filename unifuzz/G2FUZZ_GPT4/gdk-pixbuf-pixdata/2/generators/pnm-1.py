import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# ASCII PBM Example
ascii_pbm_content = """P1
# This is an example of an ASCII PBM file
4 4
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""
with open('./tmp/example_ascii.pbm', 'w') as file:
    file.write(ascii_pbm_content)

# Binary PBM Example
binary_pbm_content = bytearray([
    0x50, 0x34,       # Magic number for binary PBM file
    0x0A,             # Newline
    0x23, 0x20, 0x54, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 
    0x61, 0x6E, 0x20, 0x65, 0x78, 0x61, 0x6D, 0x70, 0x6C, 0x65,
    0x20, 0x6F, 0x66, 0x20, 0x61, 0x20, 0x62, 0x69, 0x6E, 0x61,
    0x72, 0x79, 0x20, 0x50, 0x42, 0x4D, 0x20, 0x66, 0x69, 0x6C,
    0x65, 0x0A,       # Comment line: "This is an example of a binary PBM file"
    0x34, 0x20, 0x34, 0x0A, # Width and height: 4 4
    0x00, 0b10101010, # Image data: alternating pattern
    0x00, 0b01010101,
    0x00, 0b10101010,
    0x00, 0b01010101,
])

with open('./tmp/example_binary.pbm', 'wb') as file:
    file.write(binary_pbm_content)
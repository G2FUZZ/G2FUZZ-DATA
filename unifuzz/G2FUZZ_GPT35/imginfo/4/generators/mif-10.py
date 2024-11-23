import os

# Create a directory to store the generated MIF files
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file
mif_content = """
DEPTH = 256;
WIDTH = 8;
ADDRESS_RADIX = HEX;
DATA_RADIX = BIN;

CONTENT BEGIN
0 : 00000000;
1 : 00000001;
2 : 00000010;
3 : 00000011;
4 : 00000100;
5 : 00000101;
6 : 00000110;
7 : 00000111;
8 : 00001000;
9 : 00001001;
A : 00001010;
B : 00001011;
C : 00001100;
D : 00001101;
E : 00001110;
F : 00001111;
END;
"""

# Save the generated MIF file
file_path = './tmp/generated_file.mif'
with open(file_path, 'w') as f:
    f.write(mif_content)

print(f"MIF file generated and saved at {file_path}")
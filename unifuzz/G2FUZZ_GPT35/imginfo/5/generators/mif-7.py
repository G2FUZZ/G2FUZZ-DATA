import os

# Define the table structure
table_structure = """
DEPTH = 16;
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

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the table structure to a MIF file
with open('./tmp/table_structure.mif', 'w') as file:
    file.write(table_structure)

print("MIF file with table structure generated and saved successfully!")
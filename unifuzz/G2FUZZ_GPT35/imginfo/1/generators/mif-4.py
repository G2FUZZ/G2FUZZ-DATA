import os

# Define the table structure
table_structure = """
WIDTH=8;
DEPTH=16;

ADDRESS_RADIX=UNS;
DATA_RADIX=HEX;

CONTENT BEGIN
0 : 0001;
1 : 0002;
2 : 0003;
3 : 0004;
4 : 0005;
5 : 0006;
6 : 0007;
7 : 0008;
8 : 0009;
9 : 000A;
A : 000B;
B : 000C;
C : 000D;
D : 000E;
E : 000F;
F : 0010;
END;
"""

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the table structure to a .mif file
with open('./tmp/table_structure.mif', 'w') as file:
    file.write(table_structure)

print("Table structure saved to ./tmp/table_structure.mif")
import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the content for the MIF file
version_info = """
-- Auto-generated MIF file
-- Version Information
-- Created by: My Python Script

DEPTH = 16;
WIDTH = 32;
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT BEGIN
    0 : 11223344;
    1 : A1B2C3D4;
    2 : F0E1D2C3;
    3 : 98765432;
    4 : DEADBEEF;
    5 : CAFEBABE;
    6 : 12345678;
    7 : ABCDEF01;
    8 : 87654321;
    9 : 54321098;
    A : 13579BDF;
    B : FACEFACE;
    C : F0F0F0F0;
    D : 0F0F0F0F;
    E : FFFF0000;
    F : 0000FFFF;
END;
"""

# Save the content into a file in ./tmp/ directory
file_path = './tmp/version_info.mif'
with open(file_path, 'w') as file:
    file.write(version_info)

print(f'MIF file with version information saved at: {file_path}')
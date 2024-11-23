import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file
mif_content = '''
VERSION 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  Name Char(50)
  Description Char(250)
Data

Point 1 2
  Symbol (35,0,12)
Point 2 3
  Symbol (35,0,12)
'''

# Define the file path
file_path = './tmp/compatibility_with_other_software.mif'

# Write the content to the MIF file
with open(file_path, 'w') as file:
    file.write(mif_content.strip())

print(f'MIF file created at {file_path}')
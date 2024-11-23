import os

# Define the content of the MIF file as a string
mif_content = '''Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Point 1 2
Point 3 4
'''

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the file path
file_path = './tmp/example.mif'

# Write the content to the MIF file
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file has been created at: {file_path}')
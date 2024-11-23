import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the .mif file, including the header section
mif_content = """VERSION 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer,
  Name Char(50)
Data

"""

# Specify the filename
filename = './tmp/example.mif'

# Write the content to the .mif file
with open(filename, 'w') as file:
    file.write(mif_content)

print(f'File {filename} has been created.')
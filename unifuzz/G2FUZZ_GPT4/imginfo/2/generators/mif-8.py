import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument here

# Define the path for the new MIF file
file_path = './tmp/example.mif'

# MIF file content with a header section
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 0
Columns 2
  ID Integer
  Name Char(50)
Begin
  Bounds (5000, -5000) (10000, 5000)
End
"""

# Writing the content to the MIF file
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f"MIF file with header section created at: {file_path}")
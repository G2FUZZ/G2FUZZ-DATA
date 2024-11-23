import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

  Point 1 2
"""

# Define the content of the corresponding MID file
mid_content = """1,"Example Point"
"""

# Write the MIF file
with open('./tmp/example.mif', 'w') as mif_file:
    mif_file.write(mif_content)

# Write the MID file
with open('./tmp/example.mid', 'w') as mid_file:
    mid_file.write(mid_content)

print("MIF and MID files have been generated in ./tmp/")
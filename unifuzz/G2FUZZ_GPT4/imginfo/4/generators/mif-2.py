import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file (graphical data)
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Point 1 1
Point 2 2
"""

# Define the content of the MID file (attribute data)
mid_content = """1,"First Point"
2,"Second Point"
"""

# Define file paths
mif_file_path = './tmp/example.mif'
mid_file_path = './tmp/example.mid'

# Write the MIF file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

# Write the MID file
with open(mid_file_path, 'w') as mid_file:
    mid_file.write(mid_content)

print("MIF and MID files have been generated.")
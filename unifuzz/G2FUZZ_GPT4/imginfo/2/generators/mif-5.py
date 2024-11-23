import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the path for the new .mif file
mif_file_path = os.path.join(output_dir, "multiple_geometries.mif")

# MIF content with multiple geometry types
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Point 10 10
  ID 1
  Name "Point A"

Line 20 20 30 30
  ID 2
  Name "Line B"

Pline 4
  40 40
  50 50
  60 40
  40 40
  ID 3
  Name "Polyline C"

Region  1
  5
    70 70
    80 80
    90 70
    90 60
    70 70
  ID 4
  Name "Region D"
"""

# Write the MIF content to the new file
with open(mif_file_path, "w") as mif_file:
    mif_file.write(mif_content)

print(f"File saved: {mif_file_path}")
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the content of the MIF file
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

Point 10 10
Line 10 10 20 20
Pline 3
  10 10
  20 20
  30 30
Region 1
  5
    0 0
    0 10
    10 10
    10 0
    0 0
MultiPoint 2
  15 15
  20 25
"""

# Specify the MIF file name
mif_file_name = "geometric_objects.mif"

# Full path to the MIF file
full_path = os.path.join(output_dir, mif_file_name)

# Write the content to the MIF file
with open(full_path, "w") as file:
    file.write(mif_content)

print(f"File '{mif_file_name}' has been created in '{output_dir}'.")
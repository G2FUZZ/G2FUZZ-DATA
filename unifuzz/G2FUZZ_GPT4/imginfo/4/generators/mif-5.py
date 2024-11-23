import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Define the name of the MIF file
mif_filename = os.path.join(output_dir, "example_layer.mif")

# MIF content representing a simple GIS layer
# This is a basic example; adapt it as needed for actual GIS data
mif_content = """
Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Point 1 2
Point 5 5
"""

# Write the MIF content to the file
with open(mif_filename, "w") as mif_file:
    mif_file.write(mif_content.strip())

print(f"MIF file '{mif_filename}' has been created.")
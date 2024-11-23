# Define the content of the MIF file for a region with multiple parts
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

Region 2
  5
    0.0 0.0
    0.0 100.0
    100.0 100.0
    100.0 0.0
    0.0 0.0
  5
    150.0 150.0
    150.0 250.0
    250.0 250.0
    250.0 150.0
    150.0 150.0
"""

# Define the path for the new MIF file inside the ./tmp/ directory
file_path = './tmp/region_example.mif'

# Ensure the ./tmp/ directory exists
import os
os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Corrected the typo here

# Write the content to the MIF file
with open(file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'MIF file saved to {file_path}')
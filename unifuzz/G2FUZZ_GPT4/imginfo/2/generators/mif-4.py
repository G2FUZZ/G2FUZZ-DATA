import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the name of the MIF file
filename = 'coordinates.mif'

# Define the content of the MIF file with Coordinate System Specification
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

Point 1 2
"""

# Full path to save the file
file_path = os.path.join(output_dir, filename)

# Write the content to the MIF file
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file saved at: {file_path}')
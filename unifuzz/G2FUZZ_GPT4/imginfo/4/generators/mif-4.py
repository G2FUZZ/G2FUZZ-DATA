import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the output MIF file
mif_file_path = os.path.join(output_dir, 'custom_symbolization.mif')

# MIF content with customizable symbolization
mif_content = """VERSION 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

# Define a line with custom style
Pline
  Pen (1,2,0) # Width, Pattern, Color
  Line 10 10 20 20

# Define a point with a custom marker
Point 15 15
  Symbol (35,0,12) # Shape, Color, Size
"""

# Write the MIF content to the file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f"MIF file with customizable symbolization created at: {mif_file_path}")
# Define the content to be written to the MIF file
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  Feature_Name Char(50)
  Description Char(254)
Data

  Point 1 2
    Symbol (35,0,12)
  Point 2 3
    Symbol (35,0,12)

/* Feature: Compatibility with Multiple GIS Software */
/* MIF files are widely supported across various Geographic Information System (GIS) software packages, not just MapInfo. */
/* This makes them a versatile format for interchange and use in different GIS applications. */
"""

# Path where the MIF file will be saved
file_path = './tmp/features.mif'

# Ensure the directory exists (create if it doesn't)
import os
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Writing the content to the MIF file
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file created at: {file_path}')
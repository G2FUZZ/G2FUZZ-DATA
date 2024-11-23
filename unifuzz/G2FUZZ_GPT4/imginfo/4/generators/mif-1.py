import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the new .mif file
mif_file_path = os.path.join(output_dir, 'geospatial_data.mif')

# Define some geospatial data to write into the .mif file
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

# A point representing a location (e.g., a landmark)
Point 34.0522 -118.2437
  ID 1

# A line representing a road
Line 34.0522 -118.2437 34.0522 -118.0437
  ID 2

# A polygon representing a boundary (e.g., a park or property)
Pline 3
  34.0522 -118.2437
  34.0622 -118.2537
  34.0722 -118.2437
  34.0522 -118.2437
  ID 3
"""

# Write the .mif content to the file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f"Geospatial data saved to {mif_file_path}")
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the path for the .mif file to be created
mif_file_path = os.path.join(output_dir, "projection_info.mif")

# Projection and Coordinate System Information (Example: WGS84)
projection_info = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

Point 1 1
"""

# Write the projection and coordinate system information to the .mif file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(projection_info)

print(f"Projection info MIF file has been created at: {mif_file_path}")
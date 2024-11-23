import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the new .mif file
mif_file_path = os.path.join(output_dir, 'example.mif')

# Coordinate system specification (using WGS 84 as an example)
coord_system = """CoordSys Earth Projection 1, 104
"""

# Begin writing the content to the .mif file
with open(mif_file_path, 'w') as mif_file:
    # Write the header and coordinate system specification
    mif_file.write("Version 300\n")
    mif_file.write(coord_system)
    # Optionally, add more MIF content here (e.g., region definitions, points, lines, etc.)

print(f'MIF file with coordinate system specification created at: {mif_file_path}')
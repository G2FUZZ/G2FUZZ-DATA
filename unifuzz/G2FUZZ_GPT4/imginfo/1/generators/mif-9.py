# Let's create a Python script that generates a .mif file with projection information
# and saves it into the ./tmp/ directory.

import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the filename and path
file_name = 'projection_info.mif'
file_path = os.path.join(output_dir, file_name)

# Define the projection information content to be included in the MIF file
# Here we use a common projection as an example. You might want to replace it with your specific needs.
projection_content = """
Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

  Point 1
"""

# Writing the projection information to the MIF file
with open(file_path, 'w') as file:
    file.write(projection_content)

print(f"'{file_name}' has been created with projection information in '{output_dir}'.")
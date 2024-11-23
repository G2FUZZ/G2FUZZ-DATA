import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the content of a sample MIF file with text data representation
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Point 1 2
    ID 1
    Name "Sample Point A"
Point 2 3
    ID 2
    Name "Sample Point B"
"""

# Specify the filename for the MIF file
mif_filename = 'sample.mif'

# Create and write the MIF content to the file
with open(os.path.join(output_dir, mif_filename), 'w') as mif_file:  # Corrected variable name here
    mif_file.write(mif_content)

print(f'MIF file "{mif_filename}" has been created in "{output_dir}".')
import os

# Directory where the MIF files will be saved
output_directory = './tmp/'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Content to be written to the MIF file
mif_content = '''Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

Point 10 10
'''

# MIF file name
mif_file_name = 'feature_description.mif'

# Full path to the MIF file
mif_file_path = os.path.join(output_directory, mif_file_name)

# Writing the content to the MIF file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'MIF file "{mif_file_name}" has been successfully created at "{mif_file_path}".')
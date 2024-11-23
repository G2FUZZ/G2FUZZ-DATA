import os

# Ensure the tmp directory exists
output_directory = './tmp/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the path for the MIF file
file_path = os.path.join(output_directory, 'sample_text_objects.mif')

# MIF content with text objects
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

  Text 50 50 "Label 1"
  Text 100 100 "Label 2"
  Text 150 150 "Description here"
"""

# Writing the MIF content to the file
with open(file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f"MIF file with text objects has been saved to {file_path}")
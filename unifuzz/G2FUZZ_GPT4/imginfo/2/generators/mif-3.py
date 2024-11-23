import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the path for the new MIF file
mif_file_path = os.path.join(output_dir, "example.mif")

# The content of the MIF file
mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  Name Char(50)
  Category Integer
Data

Point 100 200
  Name "Sample Point", Category 1
"""

# Writing the MIF content to the file
with open(mif_file_path, "w") as mif_file:
    mif_file.write(mif_content)

print(f"MIF file with attribute data storage created at: {mif_file_path}")
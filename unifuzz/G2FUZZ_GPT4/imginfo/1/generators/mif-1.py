import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Data to be written
point_data = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Point 34.0522 -118.2437
    1, "Los Angeles"
"""

line_data = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Line 25.276987 55.296249 25.197139 55.274111
    1, "Sample Line"
"""

polygon_data = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

Pline 4
  48.8566 2.3522
  48.8570 2.3527
  48.8570 2.3520
  48.8566 2.3522
    1, "Sample Polygon"
"""

# File names for the point, line, and polygon .mif files
file_names = ['point.mif', 'line.mif', 'polygon.mif']

# Data for each file
data_contents = [point_data, line_data, polygon_data]

# Writing data to files
for file_name, data_content in zip(file_names, data_contents):
    with open(f'./tmp/{file_name}', 'w') as file:
        file.write(data_content)

print("MIF files have been generated and saved in ./tmp/")
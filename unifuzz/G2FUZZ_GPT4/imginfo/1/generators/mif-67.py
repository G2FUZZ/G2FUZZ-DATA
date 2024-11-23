import os

def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_mif_file(output_directory, filename, mif_content):
    """Write the given content to a MIF file in the specified directory."""
    file_path = os.path.join(output_directory, filename)
    with open(file_path, 'w') as file:
        file.write(mif_content)
    print(f"MIF file has been saved to {file_path}")

def generate_mif_content():
    """Generate a more complex MIF file content."""
    header = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 3
  ID Integer
  Name Char(50)
  Description Char(100)
Data

"""
    objects = """  Region 1
    5
      0 0
      0 100
      100 100
      100 0
      0 0
    Pen (1,2,0)
    Brush (2,16777215,16777215)
  
  Line
    2
      150 150
      250 250
    Pen (1,2,0)
  
  Pline 3
    10
      300 300
      350 350
      300 400
      250 350
      300 300
    Pen (1,2,0)
  
  Text 50 50 "Label 1"
    Font ("Arial",0,12,0)
    Justify Left
  Text 100 100 "Label 2"
    Font ("Arial",0,12,0)
    Justify Center
  Text 150 150 "Description here"
    Font ("Arial",0,12,0)
    Justify Right
  
"""
    return header + objects

# Main script
output_directory = './tmp/'
filename = 'complex_structure_objects.mif'
ensure_directory_exists(output_directory)
mif_content = generate_mif_content()
write_mif_file(output_directory, filename, mif_content)
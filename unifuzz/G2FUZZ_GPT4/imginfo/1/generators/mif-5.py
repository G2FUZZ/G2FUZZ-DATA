import os

def create_mif_file(file_name, styling_info):
    """
    Creates a .mif file with the given name and styling information.
    Args:
    - file_name (str): The name of the file to create (without extension).
    - styling_info (str): The styling information to include in the file.
    """
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the path for the new .mif file
    mif_path = os.path.join('./tmp/', f'{file_name}.mif')
    
    # MIF header and data placeholder
    mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

""" + styling_info
    
    # Write the content to the .mif file
    with open(mif_path, 'w') as mif_file:
        mif_file.write(mif_content)

# Example Styling Information
styling_info = """Pline Multiple 5
    Pen (1,2,0)
    Line 10 10 20 20
    Pen (2,2,16711680)
    Line 20 20 30 30
    Pen (3,2,65280)
    Line 30 30 40 40
"""

# Create the MIF file with styling information
create_mif_file('example_styled_map', styling_info)
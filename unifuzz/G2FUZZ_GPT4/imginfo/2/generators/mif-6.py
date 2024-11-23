import os

def generate_mif_file():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the content of the MIF file
    mif_content = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 2
  ID Integer
  Name Char(50)
Data

  Point 1 2
"""
    
    # Additional content to suggest support for spatial indexing
    # This is a conceptual hint within the MIF file, as actual spatial indexing would be done outside this file
    mif_content += """\nREM Spatial Indexing Support:
REM This MIF file is designed to work with a corresponding MID file for efficient spatial querying and data retrieval.
"""
    
    # Path where the MIF file will be saved
    mif_file_path = './tmp/example.mif'
    
    # Writing the MIF file
    with open(mif_file_path, 'w') as mif_file:
        mif_file.write(mif_content)
    
    print(f"MIF file generated at: {mif_file_path}")

generate_mif_file()
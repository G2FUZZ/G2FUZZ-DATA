import os

def create_mif_file(file_name, geometries, coordinate_system="Earth Projection 1, 104", charset="WindowsLatin1", column_definitions=None):
    """
    Creates a .mif file with given name, geometries, and optional coordinate system, charset, and column definitions.
    
    Args:
    - file_name (str): The name of the file to create (without extension).
    - geometries (list of dict): A list of dictionaries where each dictionary represents a geometry with its type, styling, and coordinates.
    - coordinate_system (str, optional): The coordinate system for the map.
    - charset (str, optional): The character set to use in the file.
    - column_definitions (list of tuple, optional): List of tuples defining the columns and their data types.
    """
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define the path for the new .mif file
    mif_path = os.path.join('./tmp/', f'{file_name}.mif')
    
    # Construct the MIF header
    mif_header = f"""Version 300
Charset "{charset}"
Delimiter ","
{coordinate_system}
"""
    if column_definitions:
        mif_header += f"Columns {len(column_definitions)}\n"  # Corrected variable name here
        for col_name, col_type in column_definitions:
            mif_header += f"  {col_name} {col_type}\n"
    mif_header += "Data\n\n"
    
    # Initialize MIF content with header
    mif_content = mif_header
    
    # Append geometries to the MIF content
    for geometry in geometries:
        if geometry['type'] == 'Point':
            mif_content += f"Point {geometry['coordinates'][0]} {geometry['coordinates'][1]}\n"
        elif geometry['type'] == 'Line':
            mif_content += f"Line {geometry['coordinates'][0]} {geometry['coordinates'][1]} {geometry['coordinates'][2]} {geometry['coordinates'][3]}\n"
        elif geometry['type'] == 'Pline':
            mif_content += "Pline Multiple " + str(len(geometry['coordinates'])) + "\n"
            for line in geometry['coordinates']:
                mif_content += "  " + " ".join(map(str, line)) + "\n"
        elif geometry['type'] == 'Polygon':
            mif_content += "Pline Multiple " + str(len(geometry['coordinates']) + 1) + "\n"
            for line in geometry['coordinates']:
                mif_content += "  " + " ".join(map(str, line)) + "\n"
            # Repeat the first point to close the polygon
            mif_content += "  " + " ".join(map(str, geometry['coordinates'][0])) + "\n"
        # Include styling if present
        if 'styling' in geometry:
            mif_content += "  " + geometry['styling'] + "\n"
    
    # Write the content to the .mif file
    with open(mif_path, 'w') as mif_file:
        mif_file.write(mif_content)

# Example usage
geometries = [
    {'type': 'Point', 'coordinates': (10, 10), 'styling': 'Symbol (35,0,12)'},
    {'type': 'Line', 'coordinates': (10, 10, 20, 20), 'styling': 'Pen (1,2,0)'},
    {'type': 'Pline', 'coordinates': [(10, 10), (15, 15), (20, 15)], 'styling': 'Pen (2,2,16711680)'},
    {'type': 'Polygon', 'coordinates': [(30, 30), (35, 35), (35, 30)], 'styling': 'Brush (2,16711680,16777215)'}
]

column_definitions = [('ID', 'Integer'), ('Name', 'Char(50)')]

create_mif_file('complex_map', geometries, "Earth Projection 1, 104", "WindowsLatin1", column_definitions)
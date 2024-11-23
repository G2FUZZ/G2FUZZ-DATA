import os

def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)

def write_mif_header(mif_file, coord_sys="Earth Projection 1, 104", delimiter=","):
    """Write the header of the MIF file."""
    header = f"""Version 300
Charset "WindowsLatin1"
Delimiter "{delimiter}"
CoordSys {coord_sys}
"""
    mif_file.write(header)

def add_columns(mif_file, columns):
    """Add column definitions to the MIF file."""
    mif_file.write("Columns {}\n".format(len(columns)))
    for column in columns:
        mif_file.write("  {} {}\n".format(column[0], column[1]))
    mif_file.write("Data\n\n")

def add_point(mif_file, x, y, attributes):
    """Add a point to the MIF file."""
    mif_file.write(f"Point {x} {y}\n")
    write_attributes(mif_file, attributes)

def add_line(mif_file, x1, y1, x2, y2, attributes):
    """Add a line to the MIF file."""
    mif_file.write(f"Line {x1} {y1} {x2} {y2}\n")
    write_attributes(mif_file, attributes)

def add_polygon(mif_file, points, attributes, inner_rings=[]):
    """Add a polygon to the MIF file with optional inner rings (holes)."""
    mif_file.write(f"Pline {len(points)}\n")
    for point in points:
        mif_file.write(f"  {point[0]} {point[1]}\n")
    for ring in inner_rings:
        mif_file.write(f"  Inner {len(ring)}\n")
        for point in ring:
            mif_file.write(f"  {point[0]} {point[1]}\n")
    write_attributes(mif_file, attributes)

def add_rectangle(mif_file, x1, y1, x2, y2, attributes):
    """Add a rectangle to the MIF file."""
    mif_file.write(f"Rect {x1} {y1} {x2} {y2}\n")
    write_attributes(mif_file, attributes)

def write_attributes(mif_file, attributes):
    """Write attributes following a geospatial entity in the MIF file."""
    if attributes:
        mif_file.write("  " + " ".join([str(attr) for attr in attributes]) + "\n")

def generate_mif_file(output_dir, filename, coord_sys, columns, geospatial_data):
    """Generate a MIF file with complex geospatial data."""
    ensure_directory_exists(output_dir)
    mif_file_path = os.path.join(output_dir, filename)

    with open(mif_file_path, 'w') as mif_file:
        write_mif_header(mif_file, coord_sys=coord_sys)
        add_columns(mif_file, columns)
        
        for data in geospatial_data:
            data_type = data['type']
            attributes = data.get('attributes', [])
            
            if data_type == 'point':
                add_point(mif_file, data['x'], data['y'], attributes)
            elif data_type == 'line':
                add_line(mif_file, data['x1'], data['y1'], data['x2'], data['y2'], attributes)
            elif data_type == 'polygon':
                add_polygon(mif_file, data['points'], attributes, data.get('inner_rings', []))
            elif data_type == 'rectangle':
                add_rectangle(mif_file, data['x1'], data['y1'], data['x2'], data['y2'], attributes)
    
    print(f"Geospatial data saved to {mif_file_path}")

# Example usage
output_dir = './tmp/'
filename = 'complex_geospatial_data.mif'
coord_sys = "Earth Projection 1, 104"
columns = [("ID", "Integer"), ("Name", "Char(50)")]
geospatial_data = [
    {'type': 'point', 'x': 34.0522, 'y': -118.2437, 'attributes': [1, 'Landmark']},
    {'type': 'line', 'x1': 34.0522, 'y1': -118.2437, 'x2': 34.0522, 'y2': -118.0437, 'attributes': [2, 'Main Road']},
    {'type': 'polygon', 'points': [(34.0522, -118.2437), (34.0622, -118.2537), (34.0722, -118.2437), (34.0522, -118.2437)], 'attributes': [3, 'Park']},
    {'type': 'rectangle', 'x1': 34.0522, 'y1': -118.2437, 'x2': 34.0622, 'y2': -118.2337, 'attributes': [4, 'Building']},
]

generate_mif_file(output_dir, filename, coord_sys, columns, geospatial_data)
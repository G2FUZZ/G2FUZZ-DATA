import os

def ensure_directory_exists(directory):
    """Ensure the specified directory exists; create it if it doesn't."""
    os.makedirs(directory, exist_ok=True)

def write_mif_file(file_path, header, features):
    """Write the geographic data to a MIF file."""
    with open(file_path, 'w') as mif_file:
        mif_file.write(header)
        for feature in features:
            mif_file.write(feature)

def generate_point_feature(attributes, coordinate):
    """Generate a MIF format string for a point feature."""
    point_header = f"Point {coordinate[0]} {coordinate[1]}\n"
    data_header = "Data\n"
    attribute_data = "\"" + "\",\"".join(attributes) + "\"\n"
    return point_header + data_header + attribute_data

def generate_polyline_feature(attributes, points):
    """Generate a MIF format string for a polyline feature."""
    polyline_header = f"Pline {len(points)}\n"
    polyline_points = "\n".join([f"  {point[0]} {point[1]}" for point in points])
    data_header = "Data\n"
    attribute_data = "\"" + "\",\"".join(attributes) + "\"\n"
    return polyline_header + polyline_points + "\n" + data_header + attribute_data

def generate_polygon_feature(attributes, points):
    """Generate a MIF format string for a polygon feature."""
    polygon_header = f"Region 1\n  {len(points)}\n"
    polygon_points = "\n".join([f"  {point[0]} {point[1]}" for point in points])
    data_header = "Data\n"
    attribute_data = "\"" + "\",\"".join(attributes) + "\"\n"
    return polygon_header + polygon_points + "\n" + data_header + attribute_data

def generate_bounding_rect(points):
    """Generate a bounding rectangle for a set of points."""
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    return f"Rect {min_x} {min_y} {max_x} {max_y}\n"

# Main execution
if __name__ == "__main__":
    output_dir = "./tmp/"
    ensure_directory_exists(output_dir)
    mif_file_path = os.path.join(output_dir, "complex_geography.mif")

    # MIF Header with projection info and column definitions
    mif_header = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 3
  Name Char(40)
  Population Integer
  Type Char(10)
Data

"""

    # Define geometries with attributes
    geometries = [
        (["Point A", "500", "Point"], (2, 2)),  # Point
        (["Line A", "300", "Line"], [(3, 3), (4, 5), (6, 5)]),  # Polyline
        (["Area A", "1000", "Polygon"], [(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),  # Polygon
    ]

    # Generate feature strings for each geometry
    features = []
    for attributes, geometry in geometries:
        if len(geometry) == 2 and isinstance(geometry[0], (int, float)) and isinstance(geometry[1], (int, float)):
            features.append(generate_point_feature(attributes, geometry))
        elif all(isinstance(point, tuple) for point in geometry):
            if "Line" in attributes:
                features.append(generate_polyline_feature(attributes, geometry))
            else:
                features.append(generate_polygon_feature(attributes, geometry))
                features.append(generate_bounding_rect(geometry))

    # Write to MIF file
    write_mif_file(mif_file_path, mif_header, features)

    print(f"Complex geography MIF file has been created at: {mif_file_path}")
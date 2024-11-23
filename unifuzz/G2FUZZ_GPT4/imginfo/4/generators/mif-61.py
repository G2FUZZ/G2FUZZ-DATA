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

def generate_polygon_feature(attributes, points):
    """Generate a MIF format string for a polygon feature."""
    polygon_header = f"Pline {len(points)}\n"
    polygon_points = "\n".join([f"  {point[0]} {point[1]}" for point in points])
    data_header = "Data\n"
    attribute_data = "\"" + "\",\"".join(attributes) + "\"\n"
    return polygon_header + polygon_points + "\n" + data_header + attribute_data

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
Columns 2
  Name Char(40)
  Population Integer
Data

"""

    # Define polygons with attributes
    polygons = [
        (["Area A", "1000"], [(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),  # Square
        (["Area B", "1500"], [(6, 0), (6, 5), (11, 5), (11, 0), (6, 0)]),  # Adjacent Square
        (["Area C", "500"], [(0, 6), (0, 11), (5, 11), (5, 6), (0, 6)])  # Square above Area A
    ]

    # Generate feature strings for each polygon
    features = [generate_polygon_feature(attributes, points) for attributes, points in polygons]

    # Write to MIF file
    write_mif_file(mif_file_path, mif_header, features)

    print(f"Complex geography MIF file has been created at: {mif_file_path}")
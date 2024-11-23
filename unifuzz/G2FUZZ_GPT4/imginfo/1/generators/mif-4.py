import os

# Ensure the tmp directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the path for the MIF file
mif_file_path = os.path.join(output_dir, 'multi_geometry.mif')

# Create and write to the MIF file
with open(mif_file_path, 'w') as mif_file:
    # Write the file header
    mif_file.write("Version 300\nCharset \"WindowsLatin1\"\nDelimiter \",\"\nCoordSys Earth Projection 1, 104\nColumns 2\n  ID Integer\n  Name Char(50)\nData\n\n")
    
    # Define multiple geometries
    geometries = [
        # Point geometry (Longitude, Latitude)
        ("Point", "POINT 40.7128 -74.0060"),
        # Line geometry (Start Longitude, Start Latitude, End Longitude, End Latitude)
        ("Line", "LINE 40.7128 -74.0060 40.7138 -74.0070"),
        # Polygon geometry (A simple square for demonstration)
        ("Polygon", "POLYGON((40.7128 -74.0060, 40.7128 -74.0070, 40.7138 -74.0070, 40.7138 -74.0060, 40.7128 -74.0060))")
    ]
    
    # Write geometries to the file
    for geometry_type, geometry_data in geometries:
        if geometry_type == "Point":
            mif_file.write(f"{geometry_data}\n")
        elif geometry_type == "Line":
            mif_file.write(f"{geometry_data}\n")
        elif geometry_type == "Polygon":
            mif_file.write(f"{geometry_data}\n")
            
# Feedback to user
print(f"Generated MIF file with multiple geometries at: {mif_file_path}")
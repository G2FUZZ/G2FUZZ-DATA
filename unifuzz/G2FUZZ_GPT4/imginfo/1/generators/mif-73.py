import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the path for the new .mif file
mif_file_path = os.path.join(output_dir, 'complex_example.mif')

# Coordinate system specification (using WGS 84 as an example)
coord_system = """CoordSys Earth Projection 1, 104
"""

# Example data to write (for demonstration purposes)
features = [
    {
        'type': 'Point',
        'coordinates': (100.0, 0.5),
        'metadata': {'Symbol': (34, 0.5, 255)}  # Symbol (shape, size, color)
    },
    {
        'type': 'Line',
        'coordinates': [(1.0, 2.0), (3.0, 4.0)],
        'metadata': {'Pen': (2, 2, 65535)}  # Pen (width, pattern, color)
    },
    {
        'type': 'Pline',
        'coordinates': [(10.0, 20.0), (30.0, 40.0), (50.0, 60.0)],
        'metadata': {'Pen': (1, 1, 0)}  # Pen (width, pattern, color)
    },
    {
        'type': 'Region',
        'coordinates': [((0.0, 0.0), (0.0, 100.0), (100.0, 100.0), (100.0, 0.0))],
        'metadata': {'Brush': (2, 16777215, 0)}  # Brush (pattern, foreground color, background color)
    }
]

# Begin writing the content to the .mif file
with open(mif_file_path, 'w') as mif_file:
    # Write the header and coordinate system specification
    mif_file.write("Version 300\n")
    mif_file.write(coord_system)

    # Write features
    for feature in features:
        if feature['type'] == 'Point':
            x, y = feature['coordinates']
            symbol = feature['metadata']['Symbol']
            mif_file.write(f"Point {x} {y}\n")
            mif_file.write(f"    Symbol ({symbol[0]}, {symbol[1]}, {symbol[2]})\n")
        elif feature['type'] in ['Line', 'Pline']:
            mif_file.write(f"{feature['type']} ")
            mif_file.write(" ".join([f"{x} {y}" for x, y in feature['coordinates']]))
            mif_file.write("\n")
            pen = feature['metadata']['Pen']
            mif_file.write(f"    Pen ({pen[0]}, {pen[1]}, {pen[2]})\n")
        elif feature['type'] == 'Region':
            mif_file.write("Region 1\n")
            points_count = len(feature['coordinates'][0])
            mif_file.write(f"  {points_count}\n")
            for x, y in feature['coordinates'][0]:
                mif_file.write(f"    {x} {y}\n")
            brush = feature['metadata']['Brush']
            mif_file.write(f"    Brush ({brush[0]}, {brush[1]}, {brush[2]})\n")

print(f'MIF file with complex structures created at: {mif_file_path}')
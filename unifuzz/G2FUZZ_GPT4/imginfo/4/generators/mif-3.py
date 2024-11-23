import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Data for various geometries
point_data = "100.0 100.0"
line_data = "100.0 100.0 200.0 200.0"
polygon_data = "5\n100.0 100.0\n100.0 200.0\n200.0 200.0\n200.0 100.0\n100.0 100.0\n"
multipoint_data = "3\n100.0 100.0\n150.0 150.0\n200.0 200.0\n"

# Templates for MIF geometries
mif_templates = {
    "point.mif": f"Version 300\nCharset \"WindowsLatin1\"\nDelimiter \",\"\nCoordSys Earth Projection 1, 104\nColumns 1\n  ID Integer\nData\n\nPoint {point_data}",
    "line.mif": f"Version 300\nCharset \"WindowsLatin1\"\nDelimiter \",\"\nCoordSys Earth Projection 1, 104\nColumns 1\n  ID Integer\nData\n\nLine {line_data}",
    "polygon.mif": f"Version 300\nCharset \"WindowsLatin1\"\nDelimiter \",\"\nCoordSys Earth Projection 1, 104\nColumns 1\n  ID Integer\nData\n\nPline 5\n  {polygon_data}EndPline",
    "multipoint.mif": f"Version 300\nCharset \"WindowsLatin1\"\nDelimiter \",\"\nCoordSys Earth Projection 1, 104\nColumns 1\n  ID Integer\nData\n\nMultiPoint {multipoint_data}"
}

# Write each MIF file
for filename, content in mif_templates.items():
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write(content)

print("MIF files generated successfully.")
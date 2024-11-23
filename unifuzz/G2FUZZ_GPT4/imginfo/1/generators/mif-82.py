import os

class MIFGenerator:
    def __init__(self, filepath):
        self.filepath = filepath
        self.contents = [
            "Version 300",
            "Charset \"WindowsLatin1\"",
            "Delimiter \",\"",
            "CoordSys Earth Projection 1, 104",
            "Data"
        ]
    
    def add_columns(self, columns):
        """
        Add columns to the MIF file.
        :param columns: A list of tuples where each tuple contains the column name and type.
        """
        self.contents.insert(4, f"Columns {len(columns)}")
        for name, col_type in columns:
            self.contents.insert(5, f"  {name} {col_type}")
    
    def add_region(self, parts, attributes=None):
        """
        Add a region with multiple parts to the MIF file.
        :param parts: A list of parts where each part is a list of (x, y) tuples.
        :param attributes: A list of attribute values corresponding to the columns.
        """
        self.contents.append(f"Region {len(parts)}")
        for part in parts:
            self.contents.append(f"  {len(part)}")
            for x, y in part:
                self.contents.append(f"    {x} {y}")
        if attributes:
            self.contents.append(f"  {', '.join(map(str, attributes))}")
    
    def add_point(self, x, y, attributes=None):
        """
        Add a point to the MIF file.
        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the him.
        :param attributes: A list of attribute values corresponding to the columns.
        """
        self.contents.append(f"Point {x} {y}")
        if attributes:
            self.contents.append(f"  {', '.join(map(str, attributes))}")
    
    def save(self):
        """
        Save the contents to the specified filepath.
        """
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, 'w') as mif_file:
            mif_file.write('\n'.join(self.contents))
        print(f'MIF file saved to {self.filepath}')

# Example usage
file_path = './tmp/complex_region_example.mif'
generator = MIFGenerator(file_path)

# Adding columns for attributes
generator.add_columns([('ID', 'Integer'), ('Name', 'Char(50)')])

# Adding a region with two parts (e.g., a complex polygon with a hole)
generator.add_region([
    [(0.0, 0.0), (0.0, 100.0), (100.0, 100.0), (100.0, 0.0), (0.0, 0.0)],  # Outer boundary
    [(25.0, 25.0), (25.0, 75.0), (75.0, 75.0), (75.0, 25.0), (25.0, 25.0)]  # Hole
], attributes=[1, 'First Region'])

# Adding a point
generator.add_point(200.0, 200.0, attributes=[2, 'Lonely Point'])

# Save the MIF file
generator.save()
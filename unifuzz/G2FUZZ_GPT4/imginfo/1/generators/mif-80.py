import os

class MIFGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.header = """Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
"""
        self.columns = []
        self.data = []
        
    def add_column(self, name, data_type):
        self.columns.append((name, data_type))
        
    def add_region(self, outer_boundaries, inner_boundaries_list=[], attributes=[]):
        """
        Add a region with optional holes and attributes.
        outer_boundaries: List of tuples representing points [(x1, y1), (x2, y2), ...]
        inner_boundaries_list: List of lists of tuples, each list representing a hole in the region
        attributes: List of attribute values matching the defined columns order
        """
        region_data = f'Region {1 + len(inner_boundaries_list)}\n'
        all_boundaries = [outer_boundaries] + inner_boundaries_list
        
        for boundaries in all_boundaries:
            region_data += f'  {len(boundaries)}\n'
            for point in boundaries:
                region_data += f'    {point[0]} {point[1]}\n'
        
        self.data.append((region_data, attributes))
        
    def generate(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        # Write the MIF file
        with open(self.file_path, 'w') as mif_file:
            mif_file.write(self.header)
            
            # Columns
            if self.columns:
                mif_file.write("Columns {}\n".format(len(self.columns)))
                for name, data_type in self.columns:
                    mif_file.write(f"  {name} {data_type}\n")
                mif_file.write("Data\n\n")
            
            # Data
            for region_data, attributes in self.data:
                mif_file.write(region_data)
                if attributes:
                    mif_file.write("    Pen (1,2,0)\n")  # Example styling, can be customized
                    mif_file.write(f"    {','.join(map(str, attributes))}\n")

# Example usage
file_path = './tmp/complex_region_example.mif'
generator = MIFGenerator(file_path)

# Adding columns for attributes
generator.add_column("ID", "Integer")
generator.add_column("Name", "Char(50)")

# Adding a region with a hole and attributes
outer_boundary = [(0,0), (0,100), (100,100), (100,0), (0,0)]
inner_boundary = [(40,40), (40,60), (60,60), (60,40), (40,40)]  # A square hole
generator.add_region(outer_boundary, [inner_boundary], [1, "First Region"])

# Adding another simple region without holes and with different attributes
outer_boundary_2 = [(150,150), (150,250), (250,250), (250,150), (150,150)]
generator.add_region(outer_boundary_2, attributes=[2, "Second Region"])

# Generate the MIF file
generator.generate()

print(f'MIF file saved to {file_path}')
import os

def create_mif_file(mif_filename, features):
    """
    Creates a .mif file with given features.
    
    :param mif_filename: Path to the output MIF file.
    :param features: A list of feature dictionaries containing type, coordinates, and attributes.
    """
    header = """
Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 3
  ID Integer
  Name Char(50)
  Type Char(50)
Data
    """

    with open(mif_filename, "w") as mif_file:
        mif_file.write(header.strip() + "\n\n")

        for feature in features:
            if feature['type'] == 'Point':
                mif_file.write(f"\nPoint {feature['coords'][0]} {feature['coords'][1]}\n")
            elif feature['type'] == 'Line':
                start, end = feature['coords']
                mif_file.write(f"\nLine {start[0]} {start[1]} {end[0]} {end[1]}\n")
            elif feature['type'] == 'Pline':
                mif_file.write("\nPline\n")
                for coord in feature['coords']:
                    mif_file.write(f"  {coord[0]} {coord[1]}\n")
            elif feature['type'] == 'Region':
                mif_file.write(f"\nRegion  1\n  {len(feature['coords'])}\n")
                for coord in feature['coords']:
                    mif_file.write(f"  {coord[0]} {coord[1]}\n")
            
            # Writing attributes for each feature in the MIF file
            mif_file.write(f"    Pen (1,2,0)\n")
            mif_file.write(f"    Brush (2,0,16777215)\n")
            mif_file.write(f"    Symbol (35,0,12)\n")
            attributes = f"{feature['attributes']['ID']},'{feature['attributes']['Name']}','{feature['attributes']['Type']}'"
            mif_file.write(f"    {attributes}\n")

# Ensure the ./tmp/ directory exists
output_dir = "./tmp"
os.makedirs(output_dir, exist_ok=True)

# Define the name of the MIF file
mif_filename = os.path.join(output_dir, "complex_example.mif")

# Define features with more complex structures
features = [
    {'type': 'Point', 'coords': (10, 10), 'attributes': {'ID': 1, 'Name': 'Point Feature', 'Type': 'Landmark'}},
    {'type': 'Line', 'coords': ((15, 15), (20, 20)), 'attributes': {'ID': 2, 'Name': 'Road Segment', 'Type': 'Road'}},
    {'type': 'Pline', 'coords': [(25, 25), (30, 30), (35, 25)], 'attributes': {'ID': 3, 'Name': 'River', 'Type': 'Water'}},
    {'type': 'Region', 'coords': [(40, 40), (45, 45), (45, 40)], 'attributes': {'ID': 4, 'Name': 'Building', 'Type': 'Structure'}}
]

# Create the MIF file
create_mif_file(mif_filename, features)

print(f"MIF file '{mif_filename}' has been created with more complex structures.")
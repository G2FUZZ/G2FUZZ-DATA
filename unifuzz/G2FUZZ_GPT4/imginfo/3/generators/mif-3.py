import os

# Create the tmp directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the content of the MIF file with a sample graphic reference
mif_content = """<MIFFile 9.00> # MIF version
<Frame
    <Pen 15> # Set pen color
    <Fill 7> # Set fill color
    <PenWidth 0.5> # Set pen width
    <Rect
        <BRect 1.0 inch 1.0 inch 3.0 inch 2.0 inch> # Specify rectangle dimensions
        <Angle 0> # Rotation angle
    >
    <GroupID 1> # Assign to group
> # End Frame
<ImportObject
    <Tag `Image`>
    <ImportObFile `./image.jpg`> # Path to the image file to be included
    <ImportObRect 4.0 inch 1.0 inch 6.0 inch 3.0 inch> # Position and size
> # End ImportObject
"""

# Write the MIF content to a file
file_path = os.path.join(output_dir, 'sample.mif')  # Corrected variable name here
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file has been generated and saved to: {file_path}')
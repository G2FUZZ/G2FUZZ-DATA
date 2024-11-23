import os

# Ensure the ./tmp/ directory exists
directory = "./tmp"
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the full path for the new .mif file
file_path = os.path.join(directory, "graphics_and_images_feature.mif")

# Content to be written to the .mif file
content = """
<MIFFile 9.00> # MIF file version
<Frame
 <ID 1>
 <GroupID 2>
 <Pen 15>
 <Fill 7>
 <PenWidth  0.5>
 <ObColor `Black'>
 <DashedPattern
  <DashedStyle Solid> >
 <Angle 0>
 <BRect 1.000000 1.000000 6.500000 9.000000>
 <FrameType Below>
 <ImportObject
  <ImportObFile `path/to/your/image.jpg'>
  <ImportObRect 1.000000 1.000000 5.000000 7.000000>
 >
 <TextLine
  <String `Graphics and Images: They support embedding or linking of graphic elements and images.'>
  <TLOrigin 1.000000 1.000000>
  <TLAlignment Left>
 >
>
"""

# Write the content to the .mif file
with open(file_path, "w") as file:
    file.write(content.strip())

print(f"File 'graphics_and_images_feature.mif' has been created in the '{directory}' directory.")
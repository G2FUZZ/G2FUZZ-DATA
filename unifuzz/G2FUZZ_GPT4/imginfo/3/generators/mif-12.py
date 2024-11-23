import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file, including a description about Layered Graphics
mif_content = '''<MIFFile 9.00> # MIF version
<Units Ucm> # Unit of measure

# Frame for demonstration
<Frame
    <ID 1>
    <Pen 15>
    <Fill 7>
    <PenWidth 1.0>
    <Separation 0>
    <BRect 1.0 cm 1.0 cm 10.0 cm 5.0 cm> # Bounding rectangle
    <GroupID 1>
    <ObjLocked No> 
    <Layer
        <LayerID 1>
        <LayerName `Background`>
        <Visible Yes>
        <Locked No>
        <Printable Yes>
        <ShowInPDF Yes>
    > # End Layer
    <Layer
        <LayerID 2>
        <LayerName `Foreground`>
        <Visible Yes>
        <Locked No>
        <Printable Yes>
        <ShowInPDF Yes>
    > # End Layer
    <TextLine
        <GroupID 2>
        <TLOrigin 2.0 cm 3.0 cm>
        <TLAlignment Center>
        <String `Layered Graphics: Supporting sophisticated control over graphic elements.`>
    > # End TextLine
> # End Frame

#End of MIFFile
'''

# Save the content to a .mif file in the ./tmp/ directory
file_path = './tmp/layered_graphics_description.mif'
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'File saved at {file_path}')
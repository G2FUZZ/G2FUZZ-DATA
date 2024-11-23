import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument name here

# Define the path for the new MIF file
mif_file_path = './tmp/example.mif'

# MIF content with markers
mif_content = """
<MIFFile 9.00> # MIF file version
# Beginning of the document
<Units Ucm>
<Page
    <PageType StartOfDocument> 
    <PageTag `First Page`>
>
# Example marker for an index entry
<Marker
    <MarkerType 1> # 1 signifies an index marker
    <MarkerText `Index Entry Example`>
>
# Example marker for a technical note
<Marker
    <MarkerType 2> # Custom type; can be defined as needed
    <MarkerText `Technical Note Example`>
>
# Example marker for document navigation
<Marker
    <MarkerType 3> # Custom type; can be defined as needed
    <MarkerText `Navigation Marker Example`>
>
# End of the document
<Page
    <PageType EndOfDocument>
    <PageTag `Last Page`>
>
"""

# Writing the MIF content to a file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content.strip())

print(f'MIF file with markers has been saved to {mif_file_path}')
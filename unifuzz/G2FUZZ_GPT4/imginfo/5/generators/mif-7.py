import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file with bookmarks and tags
mif_content = """<MIFFile 9.00> # Start of the MIF file
<Bookmark 
    <Title `Chapter 1`>
    <Unique 122345>
    <PageNum 1>
> # End of Bookmark
<Bookmark 
    <Title `Chapter 1.1`>
    <Unique 122346>
    <PageNum 2>
> # End of Bookmark
# A simple tag example for a paragraph
<P 
    <PgfTag `BodyText`>
    <PgfNumString `1`>
    <ParaLine 
        <String `This is an example paragraph with a BodyText tag.`>
    > # End of ParaLine
> # End of Paragraph
</MIFFile> # End of the MIF file
"""

# Path where the MIF file will be saved
mif_file_path = './tmp/example.mif'

# Writing the content to the MIF file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'MIF file with bookmarks and tags has been generated at {mif_file_path}')
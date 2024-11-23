import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file with a hyperlink
mif_content = """
# MIF example with Hyperlink
<MIFFile 9.00> # MIF version
<Units Ucm>    # Unit of measurement

<TextFlow <ID 1> <TFTag `Body'> # Define a text flow
    <Para <PgfTag `BodyText'>   # Paragraph tag
        <String `For more information, visit our '>
        # Hyperlink
        <Hypertext
            <AType `GoToURL'>
            <URL `http://www.example.com'>
            <NewWin No> >
        <String `website.'> >
    > # End Paragraph
> # End TextFlow
<Page
    # Page attributes here
> # End Page
"""

# Save the content to a .mif file in the ./tmp/ directory
file_path = './tmp/example_hyperlink.mif'
with open(file_path, 'w') as file:
    file.write(mif_content.strip())

print(f'MIF file with hyperlink created at: {file_path}')
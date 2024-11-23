import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file with cross-references and hyperlinks
mif_content = """<MIFFile 9.00> # MIF version
# FrameMaker document containing cross-references and hyperlinks

<Para
    <PgfTag `Body`>
    <ParaLine
        <String `This document demonstrates the use of `>
        <XRef
            <XRefName `Hyperlinks`>
            <XRefSrcText `cross-references and hyperlinks`>
            <XRefSrcFile `external_source.mif`>
            <XRefFmt `PageNum`>>
        <String `. For more information, visit `>
        <Hypertext
            <HypertextCommand `openurl https://www.example.com`>
            <String `our website`>>>
        <String `. `>>
    <ParaLine
        <String `Use these features to create interactive documents.`>>>
</Para>

# End of the MIF document
<Trailer>
<EOF>"""

# Path to the new MIF file
mif_file_path = './tmp/cross_references_and_hyperlinks.mif'

# Write the MIF content to the file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'File saved as {mif_file_path}')
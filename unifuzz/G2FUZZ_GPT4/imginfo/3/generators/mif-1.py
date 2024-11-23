import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# MIF content with paragraphs and headings
mif_content = """
<MIFFile 9.00> # MIF version
<Units Uinches> # Unit of measurement
<TypesettingSpecifications>
 # Typesetting specifications
</TypesettingSpecifications>
<TextFlow
 <Para
  <PgfTag `Heading1`>
  <String `Sample Heading`>
 >
 <Para
  <PgfTag `Body`>
  <String `This is a sample paragraph to demonstrate how text can be included in a MIF file. MIF files can contain various types of text content, including paragraphs, headings, lists, and more, allowing for the representation of the structured textual information of a document.`>
 >
 <Para
  <PgfTag `Body`>
  <String `Another paragraph follows, showcasing the versatility of the MIF format in handling textual data across documents.`>
 >
> # End of TextFlow
"""

# Path to the MIF file to be created
mif_file_path = './tmp/sample.mif'

# Writing the MIF content to the file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'MIF file saved at: {mif_file_path}')
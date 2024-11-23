# Ensure the directory exists
import os

directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# MIF file content
mif_content = """<MIFFile 9.00> # MIF version
<Units Ucm>
<TextFlow <ID 1> <TFTag `Body'>
    # Main Heading
    <Para <PgfTag `Heading1'>
        <Unique 1>
        <String `Main Heading'>
    > # End of Para
    # Paragraph with character formatting
    <Para <PgfTag `Body'>
        <Unique 2>
        <String `This is an example of a paragraph in a MIF file. '>
        <Char <Font `Times New Roman'> <FSize 12> <FStyle Bold> <String `Bold text'> >
        <Char <Font `Arial'> <FSize 10> <FStyle Italic> <String ` and italic text.'> >
    > # End of Para
> # End of TextFlow
"""

# Write the MIF content to a file
file_path = os.path.join(directory, 'example.mif')
with open(file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f"MIF file created at {file_path}")
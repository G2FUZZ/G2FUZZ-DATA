import os

# Create a directory to save the generated 'mif' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'mif' file with advanced features
content = """
<MIFFile 5.00>
<ParaFormat <$parafmt>>
<CharFormat <$charfmt>>
<DefaultFont `Arial'>
<DefaultFontSize `14'>
<DefaultLeading `18'>
<DefaultAlignment `Center'>
<DefaultLPI `20'>
<DefaultLFT `40'>
<DefaultRFT `40'>
<DefaultTFT `40'>
<DefaultBFT `40'>
<DefaultColor `<CMYK 50,100,0,0>'>
<ParaTag `Heading'>
<CharTag `Bold'>
Heading text with custom color and bold formatting.

<ParaTag `Body'>
<CharTag `Normal'>
Regular body text with bullet points:
<UnorderedList>
<ListItem>
First bullet point
<ListItem>
Second bullet point

<ParaTag `Table'>
<CharTag `Normal'>
<Table 2,3>
<Row>
<Cell>Row 1, Cell 1
<Cell>Row 1, Cell 2
<Cell>Row 1, Cell 3
<Row>
<Cell>Row 2, Cell 1
<Cell>Row 2, Cell 2
<Cell>Row 2, Cell 3
"""

file_path = './tmp/advanced_example.mif'
with open(file_path, 'w') as file:
    file.write(content)

print(f"Generated 'mif' file with advanced features at: {file_path}")
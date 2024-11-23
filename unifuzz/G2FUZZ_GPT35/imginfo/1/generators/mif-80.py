import os

# Create a directory to save the generated 'mif' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'mif' file with hyperlinks, images, and tables
content = """
<MIFFile 5.00>
<ParaFormat <$parafmt>>
<CharFormat <$charfmt>>
<DefaultFont `Times-Roman'>
<DefaultFontSize `12'>
<DefaultLeading `15'>
<DefaultAlignment `Left'>
<DefaultLPI `18'>
<DefaultLFT `36'>
<DefaultRFT `36'>
<DefaultTFT `36'>
<DefaultBFT `36'>
<DefaultLinkURL `<URL "https://example.com">'>
<DefaultLinkURLName `Example Website'>

<Graphics
<Graphic
<FileName `image.jpg'>
<Width `200'>
<Height `150'>
>>

<Table
<NumColumns `3'>
<ColumnWidth `100'>
<ColumnWidth `150'>
<ColumnWidth `200'>
<Row
<Para
<Font `Times-Bold'>
<FontSize `14'>
<Alignment `Center'>
<ParaLineSpacing `18'>
<Alignment `Center'>
<Cell `Cell 1'>
<Cell `Cell 2'>
<Para
<Font `Times-Italic'>
<FontSize `12'>
<Leading `15'>
<Alignment `Right'>
<Cell `Cell 3'>
<Para
<Font `Times-Roman'>
<FontSize `10'>
<Leading `12'>
<Cell `Cell 4'>
<Para
<Font `Times-Roman'>
<FontSize `10'>
<Leading `12'>
<Cell `Cell 5'>
>>
>"""

file_path = './tmp/extended_example.mif'
with open(file_path, 'w') as file:
    file.write(content)

print(f"Generated 'mif' file with hyperlinks, images, and tables at: {file_path}")
import os

# Create a directory to save the generated 'mif' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'mif' file with hyperlinks
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
"""

file_path = './tmp/example.mif'
with open(file_path, 'w') as file:
    file.write(content)

print(f"Generated 'mif' file with hyperlinks at: {file_path}")
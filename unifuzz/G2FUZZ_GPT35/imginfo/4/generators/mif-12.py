import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the MIF file with styles
mif_content = """
<Styles>
    <StyleName = "Heading1">
        <Font Family = "Arial" Size = "14" Weight = "Bold" Color = "Black"/>
        <Paragraph Align = "Center"/>
    </StyleName>
    <StyleName = "BodyText">
        <Font Family = "Times New Roman" Size = "12" Color = "Black"/>
        <Paragraph Indent = "0.5"/>
    </StyleName>
</Styles>
"""

# Save the MIF file
with open('./tmp/styles.mif', 'w') as mif_file:
    mif_file.write(mif_content)

print("MIF file with styles generated and saved successfully.")
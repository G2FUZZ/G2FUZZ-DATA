import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate content for the 'mif' file with cross-references
content = """
<MIFFile>
    <Title>
        This is a sample 'mif' file with cross-references
    </Title>
    <Body>
        <Paragraph>
            This is the first paragraph.
        </Paragraph>
        <Paragraph>
            This paragraph contains a cross-reference to <XRef value="external_source">External Source</XRef>.
        </Paragraph>
    </Body>
    <CrossReferences>
        <XRefSrc value="external_source">
            <Para>
                This is the content of the external source.
            </Para>
        </XRefSrc>
    </CrossReferences>
</MIFFile>
"""

# Save the generated content to a 'mif' file
file_path = './tmp/sample_file.mif'
with open(file_path, 'w') as file:
    file.write(content)

print(f"Generated 'mif' file with cross-references saved at: {file_path}")
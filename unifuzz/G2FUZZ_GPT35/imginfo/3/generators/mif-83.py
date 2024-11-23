import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate mif file content with metadata and formatting options
mif_content = """
<MIFFile>
    <Metadata>
        <Author>John Doe</Author>
        <CreationDate>2022-01-01</CreationDate>
    </Metadata>
    
    <Content>
        <Heading>Introduction</Heading>
        <Paragraph>
            MIF files support various formatting options such as <Bold>bold text</Bold>, <Italic>italic text</Italic>, and <Underline>underlined text</Underline>.
        </Paragraph>
        
        <Paragraph>
            They also allow for the inclusion of <Image src="image.jpg" width="200" height="150" /> images and <Link href="https://example.com">hyperlinks</Link>.
        </Paragraph>
    </Content>
</MIFFile>
"""

# Save the generated content to a mif file
with open('./tmp/extended_mif_file.mif', 'w') as file:
    file.write(mif_content)
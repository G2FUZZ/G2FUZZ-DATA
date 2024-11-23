import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the extended MIF file with additional file features
mif_content = """
<MIFFile>
    <Metadata>
        <Title>Sample Document</Title>
        <Author>John Doe</Author>
        <CreationDate>2022-01-01</CreationDate>
    </Metadata>
    
    <Sections>
        <Section ID="1" Title="Introduction">
            <Paragraph>This is the introduction section.</Paragraph>
        </Section>
        
        <Section ID="2" Title="Main Content">
            <Paragraph>This is the main content section.</Paragraph>
            <Subsection ID="2.1" Title="Subsection 1">
                <Paragraph>This is subsection 1.</Paragraph>
            </Subsection>
            <Subsection ID="2.2" Title="Subsection 2">
                <Paragraph>This is subsection 2.</Paragraph>
            </Subsection>
        </Section>
        
        <Section ID="3" Title="Conclusion">
            <Paragraph>This is the conclusion section.</Paragraph>
        </Section>
    </Sections>
</MIFFile>
"""

# Save the extended MIF file
with open(directory + 'extended_generated_file.mif', 'w') as file:
    file.write(mif_content)

print('Extended MIF file with additional complex features generated and saved successfully.')
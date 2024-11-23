import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate MIF file with cross-references
content = """
<MIFFile>
    <Title>Sample MIF File with Cross-References</Title>
    
    <Section id="section1">
        <Title>Section 1</Title>
        <Para>This is the content of section 1.</Para>
    </Section>
    
    <Section id="section2">
        <Title>Section 2</Title>
        <Para>This is the content of section 2. Refer to <XRef Link="#section1">Section 1</XRef>.</Para>
    </Section>
</MIFFile>
"""

file_path = './tmp/sample.mif'

with open(file_path, 'w') as file:
    file.write(content)

print(f'MIF file with cross-references generated at: {file_path}')
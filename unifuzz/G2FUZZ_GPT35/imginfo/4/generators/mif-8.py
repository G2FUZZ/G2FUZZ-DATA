import os

# Create a directory to store the generated MIF files
os.makedirs('./tmp/', exist_ok=True)

# Generate MIF file with cross-references
mif_content = """
<MIFFile>
    <Title>Sample MIF File with Cross-References</Title>
    <Content>
        <Para>This is a sample paragraph with a cross-reference to <XRef Link="external_source">external source</XRef>.</Para>
    </Content>
    <CrossReferences>
        <XRef ID="external_source" Type="external" Link="https://www.example.com">External Source</XRef>
    </CrossReferences>
</MIFFile>
"""

# Save the generated MIF file
with open('./tmp/sample_mif_file.mif', 'w') as file:
    file.write(mif_content)

print("MIF file with cross-references generated and saved successfully.")
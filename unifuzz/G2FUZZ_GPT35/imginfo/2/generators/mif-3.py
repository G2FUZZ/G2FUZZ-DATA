import os

# Create a directory to save the generated files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the content for the mif files
content = """
<MIFFile 7.0>
<Prop1>
    <TagName1>DocumentProperties</TagName1>
    <Tag1>Structure</Tag1>
    <Tag2>Consists of tagged elements representing document properties and content</Tag2>
</Prop1>
<Prop2>
    <TagName2>Content</TagName2>
    <Tag1>Element1</Tag1>
    <Tag2>This is element 1 content</Tag2>
</Prop2>
</MIFFile>
"""

# Save the generated content to mif files in the './tmp/' directory
for i in range(3):
    with open(f'./tmp/file_{i+1}.mif', 'w') as f:
        f.write(content)
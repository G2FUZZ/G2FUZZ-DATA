import os

# Create the directory if it doesn't exist
directory = './tmp'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with custom schemas
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:customProperty1>Custom Value 1</custom:customProperty1>
            <custom:customProperty2>Custom Value 2</custom:customProperty2>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
"""

for i in range(3):  # Generate 3 XMP files with custom schemas
    filename = f'{directory}/custom_metadata_{i + 1}.xmp'
    with open(filename, 'w') as file:
        file.write(xmp_content)

print("XMP files with custom schemas generated successfully in the ./tmp/ directory.")
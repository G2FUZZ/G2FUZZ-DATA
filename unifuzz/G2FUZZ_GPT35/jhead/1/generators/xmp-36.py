import os

# Create the directory if it doesn't exist
directory = './tmp'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with custom schemas and more complex features
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:customProperty1>Custom Value 1</custom:customProperty1>
            <custom:customProperty2>Custom Value 2</custom:customProperty2>
            <custom:complexProperty>
                <rdf:Bag>
                    <rdf:li>Item 1</rdf:li>
                    <rdf:li>Item 2</rdf:li>
                    <rdf:li>Item 3</rdf:li>
                </rdf:Bag>
            </custom:complexProperty>
            <custom:nestedProperty>
                <custom:nestedProperty1>Nested Value 1</custom:nestedProperty1>
                <custom:nestedProperty2>Nested Value 2</custom:nestedProperty2>
                <custom:multiLevelNestedProperty>
                    <custom:level1>
                        <custom:level2>
                            <custom:level3>Deeply Nested Value</custom:level3>
                        </custom:level2>
                    </custom:level1>
                </custom:multiLevelNestedProperty>
            </custom:nestedProperty>
            <custom:arrayProperty>
                <rdf:Seq>
                    <rdf:li>Array Item 1</rdf:li>
                    <rdf:li>Array Item 2</rdf:li>
                    <rdf:li>Array Item 3</rdf:li>
                </rdf:Seq>
            </custom:arrayProperty>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
"""

for i in range(3):  # Generate 3 XMP files with custom schemas and complex features
    filename = f'{directory}/custom_metadata_{i + 1}.xmp'
    with open(filename, 'w') as file:
        file.write(xmp_content)

print("XMP files with custom schemas and more complex features generated successfully in the ./tmp/ directory.")
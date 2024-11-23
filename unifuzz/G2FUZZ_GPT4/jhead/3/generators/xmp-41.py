import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with added complexity
xmp_template = '''
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014 79.160924, 2016/09/14-01:09:01        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:dc="http://purl.org/dc/elements/1.1/"
             xmlns:xmp="http://ns.adobe.com/xap/1.0/"
             xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
             xmlns:myNamespace="http://my.namespace.com/ns/">
        <rdf:Description rdf:about=""
                         dc:format="image/jpeg"
                         dc:title="Complex Metadata Example"
                         xmp:CreatorTool="My Custom Tool"
                         xmp:CreateDate="2023-01-01T12:00:00"
                         xmpRights:UsageTerms="Copyright 2023. All rights reserved."
                         myNamespace:CustomProperty="This is a custom property value">
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>Creator Name 1</rdf:li>
                    <rdf:li>Creator Name 2</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="en">This is an English description.</rdf:li>
                    <rdf:li xml:lang="es">Esta es una descripción en español.</rdf:li>
                </rdf:Alt>
            </dc:description>
            <dc:subject>
                <rdf:Bag>
                    <rdf:li>keyword1</rdf:li>
                    <rdf:li>keyword2</rdf:li>
                </rdf:Bag>
            </dc:subject>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
'''

# Parse the XMP template
xmp_tree = ET.fromstring(xmp_template)

# Define the file path
file_path = './tmp/complex_metadata.xmp'

# Write the XMP file
with open(file_path, 'wb') as file:
    file.write(ET.tostring(xmp_tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'XMP file with complex metadata structures created at {file_path}')
import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with the Searchability feature
xmp_template = '''
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:description>By standardizing metadata, XMP enhances the searchability of digital assets, making it easier to find and organize files based on their metadata.</dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
'''

# Parse the XMP template
xmp_tree = ET.fromstring(xmp_template)

# Define the file path
file_path = './tmp/searchability_feature.xmp'

# Write the XMP file
with open(file_path, 'wb') as file:
    file.write(ET.tostring(xmp_tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'XMP file with searchability feature created at {file_path}')
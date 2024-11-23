import os
from lxml import etree

# Define the XMP template
xmp_template = '''<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Interoperability: XMP provides a standard format for metadata across different file formats, making it easier to transfer information between various applications and platforms without losing data.</rdf:li>
                </rdf:Alt>
            </dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>'''

# Parse the template
xmp_data = etree.fromstring(xmp_template)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the file path
file_path = './tmp/metadata.xmp'

# Write the XMP data to a file
with open(file_path, 'wb') as file:
    file.write(etree.tostring(xmp_data, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file saved to {file_path}")
import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces to be used in the XMP template
namespaces = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
    'Iptc4xmpExt': 'http://iptc.org/std/Iptc4xmpExt/2008-02-29/',
    'photoshop': 'http://ns.adobe.com/photoshop/1.0/'
}

# Define the XMP template with more complex features
xmp_template = '''
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
            xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
            <dc:description>By standardizing metadata, XMP enhances the searchability of digital assets.</dc:description>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Doe</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:rights>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Copyright 2023 John Doe. All rights reserved.</rdf:li>
                </rdf:Alt>
            </dc:rights>
            <dc:subject>
                <rdf:Bag>
                    <rdf:li>metadata</rdf:li>
                    <rdf:li>searchability</rdf:li>
                    <rdf:li>XMP</rdf:li>
                </rdf:Bag>
            </dc:subject>
            <Iptc4xmpExt:PersonInImage>
                <rdf:Bag>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Doe</rdf:li>
                </rdf:Bag>
            </Iptc4xmpExt:PersonInImage>
            <photoshop:Credit>John Doe Photography</photoshop:Credit>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
'''

# Parse the XMP template
xmp_tree = ET.ElementTree(ET.fromstring(xmp_template))

# Define the file path
file_path = './tmp/complex_feature.xmp'

# Write the XMP file
with open(file_path, 'wb') as file:
    file.write(ET.tostring(xmp_tree, pretty_print=True, xml_declaration=True, encoding='UTF-8', standalone=None))

print(f'XMP file with complex features created at {file_path}')
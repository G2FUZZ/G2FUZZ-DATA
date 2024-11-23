import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def create_xmp_file(file_name, metadata):
    # Create the base structure for the XMP file
    rdf = Element('rdf:RDF', {
        'xmlns:rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'xmlns:dc': "http://purl.org/dc/elements/1.1/",
        'xmlns:xmpRights': "http://ns.adobe.com/xap/1.0/rights/",
        'xmlns:xmpMM': "http://ns.adobe.com/xap/1.0/mm/",
    })

    # Description element
    description = SubElement(rdf, 'rdf:Description', {
        'rdf:about': '',
        'dc:title': metadata.get('title', ''),
        'dc:description': metadata.get('description', ''),
        'dc:creator': metadata.get('creator', ''),
        'dc:subject': ','.join(metadata.get('keywords', [])),
        'xmpRights:UsageTerms': metadata.get('license', ''),
        'xmpMM:DocumentID': metadata.get('documentID', ''),
        'xmpMM:InstanceID': metadata.get('instanceID', ''),
    })

    # Ensure the ./tmp/ directory exists
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')

    # Save the file
    tree = ElementTree(rdf)
    with open(f'./tmp/{file_name}.xmp', 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

# Example metadata
metadata_example = {
    'title': 'Example Title',
    'description': 'This is an example description.',
    'creator': 'John Doe',
    'keywords': ['example', 'metadata', 'xmp'],
    'license': 'Copyright © John Doe. All rights reserved.',
    'documentID': 'doc-123',
    'instanceID': 'instance-456',
}

create_xmp_file('example_metadata', metadata_example)
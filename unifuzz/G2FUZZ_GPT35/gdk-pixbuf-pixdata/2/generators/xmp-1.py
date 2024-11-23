import os
from xml.etree import ElementTree as ET

# Create a directory to store the xmp files
os.makedirs('./tmp/', exist_ok=True)

def generate_xmp_file(file_name, metadata):
    xmp_root = ET.Element('x:xmpmeta', attrib={'xmlns:x': 'adobe:ns:meta/'})
    rdf_description = ET.SubElement(xmp_root, 'rdf:RDF', attrib={'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    
    desc_description = ET.SubElement(rdf_description, 'rdf:Description', attrib={'xmlns:dc': 'http://purl.org/dc/elements/1.1/'})
    for key, value in metadata.items():
        ET.SubElement(desc_description, 'dc:' + key).text = value

    xmp_tree = ET.ElementTree(xmp_root)
    xmp_tree.write('./tmp/{}.xmp'.format(file_name), encoding='utf-8', xml_declaration=True)

metadata = {
    'title': 'Sample Title',
    'creator': 'John Doe',
    'subject': 'Sample Subject',
    'description': 'This is a sample XMP file.',
    'publisher': 'Publisher Name',
    'contributor': 'Contributor Name',
    'date': '2022-01-01',
}

generate_xmp_file('example_file', metadata)
import os
from xml.etree import ElementTree as ET

def generate_xmp_file(metadata_dict, file_name):
    xmp_root = ET.Element('x:xmpmeta', {'xmlns:x': 'adobe:ns:meta/'})
    rdf_description = ET.SubElement(xmp_root, 'rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    
    for key, value in metadata_dict.items():
        description = ET.SubElement(rdf_description, 'rdf:Description', {'xmlns:dc': 'http://purl.org/dc/elements/1.1/'})
        ET.SubElement(description, f'dc:{key}').text = value
    
    xmp_str = ET.tostring(xmp_root, encoding='utf-8').decode()
    
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(xmp_str)

metadata = {
    'author': 'John Doe',
    'copyright': 'Copyright 2022',
    'keywords': 'Python, XMP, Metadata',
    'description': 'Sample XMP file containing metadata information'
}

generate_xmp_file(metadata, 'sample_metadata')
import os
from xml.etree import ElementTree as ET

def generate_xmp_file(metadata_dict, file_name):
    xmp_root = ET.Element('x:xmpmeta', {'xmlns:x': 'adobe:ns:meta/'})
    
    # Add multiple namespaces to the root element
    xmp_root.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    xmp_root.set('xmlns:photoshop', 'http://ns.adobe.com/photoshop/1.0/')
    
    rdf_description = ET.SubElement(xmp_root, 'rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    
    description = ET.SubElement(rdf_description, 'rdf:Description')
    
    for key, value in metadata_dict.items():
        if key == 'author':
            author_elem = ET.SubElement(description, 'dc:creator')
            author_elem.text = value
        elif key == 'keywords':
            keywords_elem = ET.SubElement(description, 'dc:subject')
            keywords_elem.text = value
        elif key == 'copyright':
            copyright_elem = ET.SubElement(description, 'dc:rights')
            copyright_elem.text = value
        elif key == 'description':
            desc_elem = ET.SubElement(description, 'dc:description')
            desc_elem.text = value
        # Add more complex file features here based on metadata keys
        
        # Add custom namespace-specific attributes
        description.set('photoshop:Country', 'USA')
    
    xmp_str = ET.tostring(xmp_root, encoding='utf-8').decode()
    
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(xmp_str)

metadata = {
    'author': 'John Doe',
    'copyright': 'Copyright 2022',
    'keywords': 'Python, XMP, Metadata',
    'description': 'Sample XMP file containing metadata information',
    'custom_metadata': 'Custom metadata value'
}

generate_xmp_file(metadata, 'sample_metadata_extended')
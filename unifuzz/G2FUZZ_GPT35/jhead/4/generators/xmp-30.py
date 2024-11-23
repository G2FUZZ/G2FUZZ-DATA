import os
from xml.etree import ElementTree as ET

def generate_xmp_file(metadata_dict, file_name):
    xmp_root = ET.Element('x:xmpmeta', {'xmlns:x': 'adobe:ns:meta/'})
    rdf_description = ET.SubElement(xmp_root, 'rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    
    main_description = ET.SubElement(rdf_description, 'rdf:Description', {'xmlns:dc': 'http://purl.org/dc/elements/1.1/'})
    
    for key, value in metadata_dict.items():
        if key == 'author':
            author_description = ET.SubElement(main_description, 'dc:creator', {'xmlns:dc': 'http://purl.org/dc/elements/1.1/'})
            author_name = ET.SubElement(author_description, 'dc:creatorName').text = value
        elif key == 'keywords':
            keywords_description = ET.SubElement(main_description, 'dc:subject', {'xmlns:dc': 'http://purl.org/dc/elements/1.1/'})
            keywords = ET.SubElement(keywords_description, 'dc:subjectValue').text = value
        else:
            ET.SubElement(main_description, f'dc:{key}').text = value
    
    xmp_str = ET.tostring(xmp_root, encoding='utf-8').decode()
    
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(xmp_str)

metadata = {
    'author': 'John Doe',
    'copyright': 'Copyright 2022',
    'keywords': 'Python, XMP, Metadata',
    'description': 'Sample XMP file containing metadata information',
    'custom_field': 'Custom Value'
}

generate_xmp_file(metadata, 'sample_metadata')
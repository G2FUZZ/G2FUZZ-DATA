import os
from xml.etree import ElementTree as ET

def generate_complex_xmp_file(metadata_dict, file_name):
    xmp_root = ET.Element('x:xmpmeta', {'xmlns:x': 'adobe:ns:meta/'})
    rdf_description = ET.SubElement(xmp_root, 'rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    
    description = ET.SubElement(rdf_description, 'rdf:Description', {'xmlns:dc': 'http://purl.org/dc/elements/1.1/'})
    
    for key, value in metadata_dict.items():
        if key == 'custom_data':
            custom_data = ET.SubElement(description, 'customData')
            for custom_key, custom_value in value.items():
                ET.SubElement(custom_data, custom_key).text = custom_value
        else:
            ET.SubElement(description, f'dc:{key}').text = value
    
    xmp_str = ET.tostring(xmp_root, encoding='utf-8').decode()
    
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(xmp_str)

metadata = {
    'author': 'John Doe',
    'copyright': 'Copyright 2022',
    'keywords': 'Python, XMP, Metadata',
    'description': 'Sample XMP file containing metadata information',
    'custom_data': {
        'custom_field1': 'Value1',
        'custom_field2': 'Value2'
    }
}

generate_complex_xmp_file(metadata, 'sample_complex_metadata')
import os
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

def create_advanced_xmp_file(metadata, file_name):
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Base structure of an XMP file
    rdf_RDF = Element('rdf:RDF', {
        'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
        'xmlns:xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
        'xmlns:exif': 'http://ns.adobe.com/exif/1.0/',
        'xmlns:customNS': 'http://www.example.com/ns/',
        'xmlns:xmpMM': 'http://ns.adobe.com/xap/1.0/mm/',
        'xmlns:stEvt': 'http://ns.adobe.com/xap/1.0/sType/ResourceEvent#',
    })

    # Function to add elements
    def add_simple_or_structured_elements(parent, namespace, data):
        for key, value in data.items():
            if isinstance(value, dict):  # For nested structures
                bag = SubElement(parent, f'{namespace}:{key}', {'rdf:parseType': 'Resource'})
                for nested_key, nested_value in value.items():
                    nested_element = SubElement(bag, f'{namespace}:{nested_key}')
                    nested_element.text = nested_value
            elif isinstance(value, list):  # For sequences
                seq = SubElement(parent, f'{namespace}:{key}', {'rdf:parseType': 'Resource'})
                rdf_seq = SubElement(seq, 'rdf:Seq')
                for item in value:
                    li = SubElement(rdf_seq, 'rdf:li')
                    li.text = item
            else:  # Simple elements
                element = SubElement(parent, f'{namespace}:{key}')
                element.text = value

    # Adding sections with complex structures
    for section, ns_data in metadata.items():
        description = SubElement(rdf_RDF, 'rdf:Description')
        description.set('rdf:about', '')
        add_simple_or_structured_elements(description, section, ns_data)

    # Convert the XML structure to a string and format it
    rough_string = tostring(rdf_RDF, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_string = reparsed.toprettyxml(indent="  ")

    # Write the pretty XML string to a file
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(pretty_string)

# Example metadata dictionary
metadata = {
    'dc': {
        'title': 'Example Title',
        'creator': ['John Doe', 'Jane Doe'],
        'description': 'A detailed description here.',
    },
    # Add more metadata as needed
}

create_advanced_xmp_file(metadata, 'example_metadata_sidecar')
import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.dom.minidom

def create_complex_xmp_file(metadata, file_name):
    # Base structure of an XMP file
    rdf_RDF = Element('rdf:RDF', {
        'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
        'xmlns:xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
        'xmlns:exif': 'http://ns.adobe.com/exif/1.0/',
        'xmlns:customNS': 'http://www.example.com/ns/',
    })
    
    # Dublin Core description section
    dc_description = SubElement(rdf_RDF, 'rdf:Description')
    dc_description.set('rdf:about', '')
    for key, value in metadata['dc'].items():
        element = SubElement(dc_description, f'dc:{key}')
        element.text = value
    
    # Rights Management section
    rights_description = SubElement(rdf_RDF, 'rdf:Description')
    rights_description.set('rdf:about', '')
    for key, value in metadata['xmpRights'].items():
        element = SubElement(rights_description, f'xmpRights:{key}')
        element.text = value

    # EXIF section (example for nested elements)
    exif_description = SubElement(rdf_RDF, 'rdf:Description')
    exif_description.set('rdf:about', '')
    for key, value in metadata['exif'].items():
        if isinstance(value, dict):  # For nested structures
            bag = SubElement(exif_description, f'exif:{key}', {'rdf:parseType': 'Resource'})
            for nested_key, nested_value in value.items():
                nested_element = SubElement(bag, f'exif:{nested_key}')
                nested_element.text = nested_value
        else:
            element = SubElement(exif_description, f'exif:{key}')
            element.text = value
    
    # Custom namespace section
    custom_description = SubElement(rdf_RDF, 'rdf:Description')
    custom_description.set('rdf:about', '')
    for key, value in metadata['customNS'].items():
        element = SubElement(custom_description, f'customNS:{key}')
        element.text = value
    
    # Convert the XML structure to a string and format it
    rough_string = tostring(rdf_RDF, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_string = reparsed.toprettyxml(indent="  ")
    
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Write the pretty XML string to a file
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(pretty_string)

# Example metadata dictionary
metadata = {
    'dc': {
        'title': 'Example Title',
        'creator': 'John Doe',
        'description': 'A sample description here.',
    },
    'xmpRights': {
        'UsageTerms': 'This is a sample usage term.',
        'WebStatement': 'http://www.example.com',
    },
    'exif': {
        'Make': 'Example Make',
        'Model': 'Example Model',
        'UserComment': {
            'Comment': 'A user comment here.',
        }
    },
    'customNS': {
        'customField1': 'Custom value 1',
        'customField2': 'Custom value 2',
    }
}

create_complex_xmp_file(metadata, 'complex_metadata_sidecar')
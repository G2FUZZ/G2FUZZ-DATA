import os
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_xmp_feature():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Create the base of the XMP structure
    rdf = Element('rdf:RDF')
    rdf.set('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    
    # Create a Description element
    description = SubElement(rdf, 'rdf:Description')
    description.set('rdf:about', '')
    description.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    
    # Add a feature about batch processing
    feature = SubElement(description, 'dc:description')
    feature.text = "Batch Processing: XMP supports batch processing of metadata, allowing for the efficient updating, tagging, and management of large volumes of digital assets. This is particularly useful for photographers, publishers, and digital content creators who need to manage extensive collections."
    
    # Generate pretty-printed XML string
    xml_str = prettify(rdf)
    
    # Write to file
    file_path = './tmp/batch_processing_feature.xmp'
    with open(file_path, 'w') as file:
        file.write(xml_str)
    
    print(f'XMP file created at: {file_path}')

create_xmp_feature()
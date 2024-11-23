import os
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_complex_xmp_feature():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Create the base of the XMP structure
    rdf = Element('rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    
    # Create multiple Description elements with various namespaces and properties
    for i in range(1, 4):
        description = SubElement(rdf, 'rdf:Description', {
            'rdf:about': f"http://example.com/descriptions/{i}",
            f'xmlns:dc{i}': f"http://purl.org/dc/elements/1.{i}/",
            f'xmlns:custom{i}': f"http://example.com/custom/{i}/"
        })
        
        # Add different features with nested elements
        title = SubElement(description, f'dc{i}:title')
        title.text = f"Title for Description {i}"
        
        creator = SubElement(description, f'dc{i}:creator')
        creator.text = f"Creator Name {i}"
        
        # Custom nested elements
        custom_feature = SubElement(description, f'custom{i}:feature')
        custom_feature.text = f"Custom Feature {i} Text"
        
        custom_details = SubElement(description, f'custom{i}:details')
        for detail in range(1, 4):
            detail_sub = SubElement(custom_details, f'custom{i}:detail', {'id': str(detail)})
            detail_sub.text = f"Detail {detail} for Custom Feature {i}"
    
    # Generate pretty-printed XML string
    xml_str = prettify(rdf)
    
    # Write to file
    file_path = './tmp/complex_features.xmp'
    with open(file_path, 'w') as file:
        file.write(xml_str)
    
    print(f'XMP file created at: {file_path}')

create_complex_xmp_feature()
import os
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_advanced_xmp_feature():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Create the base of the XMP structure
    rdf = Element('rdf:RDF')
    rdf.set('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    rdf.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    rdf.set('xmlns:xmpRights', 'http://ns.adobe.com/xap/1.0/rights/')
    rdf.set('xmlns:cc', 'http://creativecommons.org/ns#')
    rdf.set('xmlns:myNS', 'http://www.example.com/ns#')  # Custom namespace for additional metadata
    
    # Create a Description element for basic metadata
    basic_description = SubElement(rdf, 'rdf:Description')
    basic_description.set('rdf:about', '')
    
    title = SubElement(basic_description, 'dc:title')
    title.text = "Example Title"
    
    creator = SubElement(basic_description, 'dc:creator')
    creator.text = "John Doe"
    
    description = SubElement(basic_description, 'dc:description')
    description.text = "This is an example of embedding complex metadata within an XMP file."
    
    # Create another Description for rights management
    rights_description = SubElement(rdf, 'rdf:Description')
    rights_description.set('rdf:about', '')
    
    rights = SubElement(rights_description, 'xmpRights:UsageTerms')
    rights.text = "This content is available under specific terms and conditions."
    
    license = SubElement(rights_description, 'cc:license')
    license.text = "http://creativecommons.org/licenses/by-nc/4.0/"
    
    # Add custom metadata
    custom_description = SubElement(rdf, 'rdf:Description')
    custom_description.set('rdf:about', '')
    
    custom_feature = SubElement(custom_description, 'myNS:customFeature')
    custom_feature.text = "This is a custom metadata feature to demonstrate extensibility."
    
    # Generate pretty-printed XML string
    xml_str = prettify(rdf)
    
    # Write to file
    file_path = './tmp/advanced_feature.xmp'
    with open(file_path, 'w') as file:
        file.write(xml_str)
    
    print(f'Advanced XMP file created at: {file_path}')

create_advanced_xmp_feature()
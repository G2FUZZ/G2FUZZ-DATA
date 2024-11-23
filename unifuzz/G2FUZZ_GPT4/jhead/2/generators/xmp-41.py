import os
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_complex_xmp_file():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Create the base of the XMP structure
    rdf = Element('rdf:RDF')
    rdf.set('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    rdf.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    rdf.set('xmlns:xmp', 'http://ns.adobe.com/xap/1.0/')
    
    # Create multiple Description elements
    # Description for basic metadata
    description1 = SubElement(rdf, 'rdf:Description')
    description1.set('rdf:about', '')
    description1.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    
    title = SubElement(description1, 'dc:title')
    title.text = "Complex XMP Example"
    
    description = SubElement(description1, 'dc:description')
    description.text = "This example demonstrates more complex structures within XMP files."
    
    # Description for creator details
    description2 = SubElement(rdf, 'rdf:Description')
    description2.set('rdf:about', '')
    description2.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    
    creators = SubElement(description2, 'dc:creator')
    seq = SubElement(creators, 'rdf:Seq')
    for creator in ['Creator One', 'Creator Two', 'Creator Three']:
        li = SubElement(seq, 'rdf:li')
        li.text = creator
    
    # Description for keywords using rdf:Bag for an unordered list
    description3 = SubElement(rdf, 'rdf:Description')
    description3.set('rdf:about', '')
    description3.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    
    keywords = SubElement(description3, 'dc:subject')
    bag = SubElement(keywords, 'rdf:Bag')
    for keyword in ['XMP', 'Metadata', 'Digital Asset Management']:
        li = SubElement(bag, 'rdf:li')
        li.text = keyword
    
    # Generate pretty-printed XML string
    xml_str = prettify(rdf)
    
    # Write to file
    file_path = './tmp/complex_xmp_example.xmp'
    with open(file_path, 'w') as file:
        file.write(xml_str)
    
    print(f'Complex XMP file created at: {file_path}')

create_complex_xmp_file()
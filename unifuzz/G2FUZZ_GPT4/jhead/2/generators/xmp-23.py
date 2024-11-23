import os
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_complex_xmp():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Create the base of the XMP structure
    rdf = Element('rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                              'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
                              'xmlns:xmp': 'http://ns.adobe.com/xap/1.0/',
                              'xmlns:dcmm': 'http://purl.org/dc/dcmitype/',
                              'xmlns:photoshop': 'http://ns.adobe.com/photoshop/1.0/'})
    
    # Create a Description element for generic information
    description1 = SubElement(rdf, 'rdf:Description')
    description1.set('rdf:about', '')
    
    # Add a title
    title = SubElement(description1, 'dc:title')
    title.text = "Advanced Photo Editing Techniques"
    
    # Add a creator
    creator = SubElement(description1, 'dc:creator')
    creator_seq = SubElement(creator, 'rdf:Seq')
    creator_name = SubElement(creator_seq, 'rdf:li')
    creator_name.text = "Jane Doe"
    
    # Add an identifier
    identifier = SubElement(description1, 'dc:identifier')
    identifier.text = "AD12345678"
    
    # Add rights information
    rights = SubElement(description1, 'dc:rights')
    rights.text = "© 2023 Jane Doe. All rights reserved."
    
    # Create a second Description element for software-specific information
    description2 = SubElement(rdf, 'rdf:Description')
    description2.set('rdf:about', '')
    
    # Add software information
    software = SubElement(description2, 'xmp:CreatorTool')
    software.text = "Adobe Photoshop 2023"
    
    # Add a feature about batch processing using a custom namespace
    batch_processing = SubElement(description2, 'photoshop:BatchProcess')
    batch_processing.text = "True"
    
    # Add an advanced feature
    advanced_feature = SubElement(description2, 'photoshop:AdvancedFeature')
    advanced_feature.text = "HDR Processing and AI Enhancements"
    
    # Generate pretty-printed XML string
    xml_str = prettify(rdf)
    
    # Write to file
    file_path = './tmp/advanced_photo_editing.xmp'
    with open(file_path, 'w') as file:
        file.write(xml_str)
    
    print(f'Complex XMP file created at: {file_path}')

create_complex_xmp()
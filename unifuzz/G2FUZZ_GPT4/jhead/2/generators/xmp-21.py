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

    # Create the base of the XMP structure with namespaces
    rdf = Element('rdf:RDF', {
        'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
        'xmlns:xmp': 'http://ns.adobe.com/xap/1.0/',
        'xmlns:exif': 'http://ns.adobe.com/exif/1.0/',
        'xmlns:tiff': 'http://ns.adobe.com/tiff/1.0/'
    })

    # Create a Description element with multiple attributes
    description = SubElement(rdf, 'rdf:Description', {
        'rdf:about': '',
        'dc:format': 'image/jpeg',
        'xmp:CreatorTool': 'Custom XMP Writer'
    })

    # Add creator information
    creators = SubElement(description, 'dc:creator')
    creator_seq = SubElement(creators, 'rdf:Seq')
    creator_li = SubElement(creator_seq, 'rdf:li')
    creator_li.text = "John Doe"

    # Add rights information with multiple languages
    rights = SubElement(description, 'dc:rights')
    rights_bag = SubElement(rights, 'rdf:Alt')
    rights_en = SubElement(rights_bag, 'rdf:li', {'xml:lang': 'en'})
    rights_en.text = "© John Doe. All rights reserved."
    rights_fr = SubElement(rights_bag, 'rdf:li', {'xml:lang': 'fr'})
    rights_fr.text = "© John Doe. Tous droits réservés."

    # Add subject tags
    subjects = SubElement(description, 'dc:subject')
    subject_bag = SubElement(subjects, 'rdf:Bag')
    subject_li1 = SubElement(subject_bag, 'rdf:li')
    subject_li1.text = "photography"
    subject_li2 = SubElement(subject_bag, 'rdf:li')
    subject_li2.text = "nature"

    # Add complex nested structures for camera information
    camera_make = SubElement(description, 'tiff:Make')
    camera_make.text = "Canon"
    camera_model = SubElement(description, 'tiff:Model')
    camera_model.text = "Canon EOS 5D Mark IV"
    
    # Add EXIF data
    exposure_time = SubElement(description, 'exif:ExposureTime')
    exposure_time.text = "1/60"
    f_number = SubElement(description, 'exif:FNumber')
    f_number.text = "2.8"
    
    # Generate pretty-printed XML string
    xml_str = prettify(rdf)

    # Write to file
    file_path = './tmp/complex_metadata.xmp'
    with open(file_path, 'w') as file:
        file.write(xml_str)

    print(f'Complex XMP file created at: {file_path}')

create_complex_xmp()
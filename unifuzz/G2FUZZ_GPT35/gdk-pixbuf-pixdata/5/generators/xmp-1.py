import os
from xml.etree.ElementTree import Element, SubElement, tostring

# Create a function to generate XMP files with metadata
def generate_xmp_file(metadata):
    root = Element('x:xmpmeta', attrib={'xmlns:x': 'adobe:ns:meta/'})
    rdf = SubElement(root, 'rdf:RDF', attrib={'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
    description = SubElement(rdf, 'rdf:Description')

    for key, value in metadata.items():
        SubElement(description, key).text = value

    xmp_content = tostring(root, encoding='utf-8').decode()

    return xmp_content

# Define metadata for the XMP file
metadata = {
    'dc:creator': 'John Doe',
    'dc:rights': 'Copyright 2022',
    'dc:subject': 'Python, XMP, Metadata',
    'dc:description': 'Sample XMP file with metadata'
}

# Create a directory to store the XMP files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save XMP file with metadata
xmp_content = generate_xmp_file(metadata)
with open('./tmp/sample.xmp', 'w') as file:
    file.write(xmp_content)

print('XMP file generated successfully.')
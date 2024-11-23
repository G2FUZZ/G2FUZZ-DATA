import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template
def create_xmp_content():
    rdf = Element('rdf:RDF', {
        'xmlns:rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'xmlns:dc': "http://purl.org/dc/elements/1.1/"
    })

    description = SubElement(rdf, 'rdf:Description', {
        'rdf:about': "",
        'dc:format': "application/pdf",
        'dc:description': "XMP can be embedded into the file it describes, allowing the metadata to travel with the file through various systems and platforms. This ensures that the information is always available and not easily separated from the file."
    })

    return rdf

# Generate XMP content
xmp_content = create_xmp_content()

# Save the XMP file
xmp_file_path = './tmp/example.xmp'
with open(xmp_file_path, 'wb') as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    ElementTree(xmp_content).write(f, encoding='utf-8', xml_declaration=False)

print(f"XMP file saved to {xmp_file_path}")
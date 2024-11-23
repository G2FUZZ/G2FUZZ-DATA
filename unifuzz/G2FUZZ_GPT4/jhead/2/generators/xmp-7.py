import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the root element with namespace declarations
xmp_root = Element('xmpmeta')
xmp_root.set('xmlns:x', 'adobe:ns:meta/')
xmp_root.set('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')

# Add rdf:RDF element
rdf = SubElement(xmp_root, 'rdf:RDF')

# Add rdf:Description element with compatibility notes
description = SubElement(rdf, 'rdf:Description', {
    'rdf:about': '',
    'xmlns:xmp': 'http://ns.adobe.com/xap/1.0/',
    'xmp:CreatorTool': 'Custom Python Script',
    'xmp:CreateDate': '2023-01-01T12:00:00Z'
})
notes = SubElement(description, 'xmp:Notes')
notes.text = "7. **Compatibility with Industry Standards**: XMP is designed to be compatible with other metadata standards, such as IPTC (International Press Telecommunications Council) and EXIF (Exchangeable Image File Format), ensuring that metadata remains consistent across different formats and workflows."

# Convert the created XML structure to a string
raw_xml = tostring(xmp_root, 'utf-8')

# Use parseString to convert the raw XML string to a DOM object, then pretty print it
pretty_xml = parseString(raw_xml).toprettyxml(indent="    ")

# Save the pretty XML to a file
with open('./tmp/metadata.xmp', 'w', encoding='utf-8') as file:
    file.write(pretty_xml)

print("XMP file successfully created at './tmp/metadata.xmp'")
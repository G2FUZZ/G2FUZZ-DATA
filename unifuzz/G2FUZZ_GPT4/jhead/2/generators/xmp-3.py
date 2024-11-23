from lxml import etree
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Namespace map
NS_MAP = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'xmp': "http://ns.adobe.com/xap/1.0/"
}

# Create RDF skeleton
rdf = etree.Element(etree.QName(NS_MAP['rdf'], 'RDF'), nsmap=NS_MAP)

# Create a Description element within RDF
description = etree.SubElement(
    rdf,
    etree.QName(NS_MAP['rdf'], "Description"),
    {
        etree.QName(NS_MAP['rdf'], "about"): "",
        etree.QName(NS_MAP['xmp'], "Creator"): "John Doe",
        etree.QName(NS_MAP['xmp'], "Title"): "Sample XMP File",
        etree.QName(NS_MAP['xmp'], "Date"): "2023-01-01"
    },
    nsmap=NS_MAP
)

# Convert to string
rdf_str = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding="UTF-8")

# Write to file
file_path = './tmp/sample.xmp'
with open(file_path, 'wb') as file:
    file.write(rdf_str)

print(f"XMP file generated at: {file_path}")
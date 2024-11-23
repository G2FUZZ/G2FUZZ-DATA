import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the namespaces to be used
NS_RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
NS_DC = "http://purl.org/dc/elements/1.1/"

# Create an RDF element
rdf = etree.Element(f"{{{NS_RDF}}}RDF", nsmap={'rdf': NS_RDF})

# Create a Description element with the DC namespace
description = etree.SubElement(rdf, f"{{{NS_RDF}}}Description", {
    f"{{{NS_RDF}}}about": "example",
    f"{{{NS_DC}}}title": "XMP RDF Example",
    f"{{{NS_DC}}}creator": "Python Script",
    f"{{{NS_DC}}}description": "An example of XMP file with RDF structure",
})

# Pretty print the output XML
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Define the file path
file_path = './tmp/example.xmp'

# Write the XML to an XMP file
with open(file_path, 'wb') as file:
    file.write(xml_bytes)

print(f"XMP file generated at: {file_path}")
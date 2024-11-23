import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata
metadata = {
    'copyright': 'Copyright 2023, Example Company',
    'keywords': ['example', 'metadata', 'xmp'],
    'description': 'An example of XMP file with rich metadata.',
    'rating': '5'
}

# Create the root element
rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap={'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#"})

# Create a Description element for the metadata
description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")

# Add metadata fields to the Description
for key, value in metadata.items():
    if isinstance(value, list):  # For fields with multiple values like keywords
        for item in value:
            field = etree.SubElement(description, key)
            field.text = item
    else:
        field = etree.SubElement(description, key)
        field.text = value

# Convert the XML structure to a string
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Save the XML to an XMP file
xmp_file_path = './tmp/example_metadata.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xml_bytes)

print(f"XMP file saved to {xmp_file_path}")
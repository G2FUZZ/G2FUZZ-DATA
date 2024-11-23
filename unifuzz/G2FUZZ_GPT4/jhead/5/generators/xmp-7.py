from lxml import etree

# Define the XMP metadata content
content = """
7. **Integration with Adobe Products**: Developed by Adobe, XMP is tightly integrated with Adobe's suite of products. This allows for seamless creation, viewing, and editing of XMP metadata within Adobe applications like Photoshop, Lightroom, and Acrobat.
"""

# Correctly create an XML structure for XMP with namespaces
nsmap = {'x': 'adobe:ns:meta/', 'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
xmp_data = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap=nsmap)  # Use the namespace URI directly in the tag
rdf = etree.SubElement(xmp_data, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=nsmap)

# Define a description element with your content
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=nsmap)
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')
description.text = etree.CDATA(content)

# Convert the XML structure to a string
xmp_str = etree.tostring(xmp_data, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Define the output file path
output_file = './tmp/metadata.xmp'

# Save the XMP data to a file
with open(output_file, 'wb') as file:
    file.write(xmp_str)

print(f'XMP file saved to {output_file}')
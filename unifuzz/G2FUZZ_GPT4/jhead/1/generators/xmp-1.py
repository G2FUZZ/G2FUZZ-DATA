from lxml import etree
import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Namespace map for XMP
ns_map = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'xmp': "http://ns.adobe.com/xap/1.0/"
}

# Create the root element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=ns_map)

# Create a Description element
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description')
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')

# Add interoperability feature
interoperability = etree.SubElement(description, '{http://ns.adobe.com/xap/1.0/}Interoperability')
interoperability.text = 'XMP is designed to work across different formats, allowing metadata to be shared among different applications, devices, and systems without loss of information.'

# Serialize the XMP data
xmp_data = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Save the XMP data to a file
file_path = './tmp/interoperability_feature.xmp'
with open(file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f'XMP file created at {file_path}')
import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Namespace map to simplify the etree Element creation
NS_MAP = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'ex': 'http://example.com/xmp/1.0/',
    'dc': 'http://purl.org/dc/elements/1.1/',
}

# Create the root element of the XMP data
xmpmeta = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap={'x': NS_MAP['x']})
rdf_RDF = etree.SubElement(xmpmeta, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=NS_MAP)

# First Description: Basic metadata with hierarchical properties
rdf_Description1 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=NS_MAP)
rdf_Description1.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')
title_alt = etree.SubElement(rdf_Description1, '{http://purl.org/dc/elements/1.1/}title')
rdf_Alt = etree.SubElement(title_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')
for lang, title in [("en", "Complex XMP Example"), ("fr", "Exemple XMP Complexe")]:
    rdf_li = etree.SubElement(rdf_Alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', {'{http://www.w3.org/XML/1998/namespace}lang': lang})
    rdf_li.text = title

# Second Description: Custom structured properties
rdf_Description2 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=NS_MAP)
custom_Struct = etree.SubElement(rdf_Description2, '{http://example.com/xmp/1.0/}CustomStructure')
ex_Property = etree.SubElement(custom_Struct, '{http://example.com/xmp/1.0/}Property')
ex_Property.text = "Custom Value"
ex_NestedStruct = etree.SubElement(custom_Struct, '{http://example.com/xmp/1.0/}NestedStructure')
ex_NestedProperty = etree.SubElement(ex_NestedStruct, '{http://example.com/xmp/1.0/}NestedProperty')
ex_NestedProperty.text = "Nested Value"

# Convert the XML tree into a string
xmp_content = etree.tostring(xmpmeta, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Define the file path
file_path = './tmp/complex_custom_xmp_file.xmp'

# Write the content to an XMP file
with open(file_path, 'wb') as file:
    file.write(xmp_content)

print(f'XMP file saved at {file_path}')
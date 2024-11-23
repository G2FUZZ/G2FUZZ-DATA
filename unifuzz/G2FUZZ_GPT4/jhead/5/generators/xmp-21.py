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
    'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
}

# Create the root element of the XMP data
xmpmeta = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap={'x': NS_MAP['x']})
rdf_RDF = etree.SubElement(xmpmeta, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=NS_MAP)

# First Description: Basic metadata with hierarchical properties and qualifiers
rdf_Description1 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=NS_MAP)
rdf_Description1.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')
title_alt = etree.SubElement(rdf_Description1, '{http://purl.org/dc/elements/1.1/}title')
rdf_Alt = etree.SubElement(title_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')
for lang, title in [("en", "Advanced XMP Example"), ("fr", "Exemple XMP Avancé"), ("es", "Ejemplo Avanzado de XMP")]:
    rdf_li = etree.SubElement(rdf_Alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', {'{http://www.w3.org/XML/1998/namespace}lang': lang})
    rdf_li.text = title

# Second Description: Extended custom structured properties with arrays and nested elements
rdf_Description2 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=NS_MAP)
custom_Struct = etree.SubElement(rdf_Description2, '{http://example.com/xmp/1.0/}ExtendedCustomStructure')
ex_PropertyArray = etree.SubElement(custom_Struct, '{http://example.com/xmp/1.0/}PropertyArray', nsmap=NS_MAP)
rdf_Bag = etree.SubElement(ex_PropertyArray, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')
for value in ["Array Value 1", "Array Value 2", "Array Value 3"]:
    rdf_li = etree.SubElement(rdf_Bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    rdf_li.text = value
ex_PropertyWithQualifier = etree.SubElement(custom_Struct, '{http://example.com/xmp/1.0/}PropertyWithQualifier')
ex_PropertyWithQualifier.text = "Qualified Value"
ex_Qualifier = etree.SubElement(ex_PropertyWithQualifier, '{http://example.com/xmp/1.0/}Qualifier')
ex_Qualifier.text = "Qualifying Information"

# Third Description: Rights Management Information
rdf_Description3 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=NS_MAP)
rights_UsageTerms = etree.SubElement(rdf_Description3, '{http://ns.adobe.com/xap/1.0/rights/}UsageTerms')
rdf_Alt = etree.SubElement(rights_UsageTerms, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')
for lang, terms in [("en", "For demonstration purposes only."), ("fr", "Uniquement à des fins de démonstration.")]:
    rdf_li = etree.SubElement(rdf_Alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', {'{http://www.w3.org/XML/1998/namespace}lang': lang})
    rdf_li.text = terms

# Convert the XML tree into a string
xmp_content = etree.tostring(xmpmeta, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Define the file path
file_path = './tmp/advanced_custom_xmp_file.xmp'

# Write the content to an XMP file
with open(file_path, 'wb') as file:
    file.write(xmp_content)

print(f'XMP file saved at {file_path}')
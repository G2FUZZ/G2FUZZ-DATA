import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Namespace map to simplify the etree Element creation
NS_MAP = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'ex': 'http://example.com/xmp/1.0/',
}

# Create the root element of the XMP data
xmpmeta = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap={'x': NS_MAP['x']})
rdf_RDF = etree.SubElement(xmpmeta, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap={'rdf': NS_MAP['rdf']})

# First Description: Basic metadata
rdf_Description1 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap={'rdf': NS_MAP['rdf']})
rdf_Description1.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')
rdf_Description1.set('{http://example.com/xmp/1.0/}Title', 'Complex XMP Example')
rdf_Description1.set('{http://example.com/xmp/1.0/}Creator', 'John Doe')

# Second Description: Features with rdf:Seq for ordered list
rdf_Description2 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap={'rdf': NS_MAP['rdf']})
ex_Features = etree.SubElement(rdf_Description2, '{http://example.com/xmp/1.0/}Features')
rdf_Seq = etree.SubElement(ex_Features, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq')
for feature in ["Structured Metadata", "Interoperability", "Extensibility"]:
    rdf_li = etree.SubElement(rdf_Seq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    rdf_li.text = feature

# Third Description: Keywords with rdf:Bag for unordered collection
rdf_Description3 = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap={'rdf': NS_MAP['rdf']})
ex_Keywords = etree.SubElement(rdf_Description3, '{http://example.com/xmp/1.0/}Keywords')
rdf_Bag = etree.SubElement(ex_Keywords, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')
for keyword in ["XMP", "Metadata", "RDF"]:
    rdf_li = etree.SubElement(rdf_Bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    rdf_li.text = keyword

# Convert the XML tree into a string
xmp_content = etree.tostring(xmpmeta, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Define the file path
file_path = './tmp/complex_feature_xmp_file.xmp'

# Write the content to an XMP file
with open(file_path, 'wb') as file:
    file.write(xmp_content)

print(f'XMP file saved at {file_path}')
import os
from lxml import etree

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create an XML structure for the XMP data
nsmap = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmp': 'http://ns.adobe.com/xap/1.0/'
}
xmp_root = etree.Element('{http://ns.adobe.com/xap/1.0/}xmpmeta', nsmap=nsmap)
rdf_RDF = etree.SubElement(xmp_root, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF')

# Create a description element
rdf_Description = etree.SubElement(rdf_RDF, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description')

# Add a simple string property
title = etree.SubElement(rdf_Description, '{http://purl.org/dc/elements/1.1/}title')
title.text = "Example Title"

# Add a structured object property (Creator with details)
creator = etree.SubElement(rdf_Description, '{http://ns.adobe.com/xap/1.0/}Creator')
creator_detail = etree.SubElement(creator, '{http://ns.adobe.com/xap/1.0/}Seq')
li = etree.SubElement(creator_detail, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
li.text = "John Doe"

# Add an array property (Keywords)
keywords = etree.SubElement(rdf_Description, '{http://ns.adobe.com/xap/1.0/}Keywords')
keywords_detail = etree.SubElement(keywords, '{http://ns.adobe.com/xap/1.0/}Bag')
for keyword in ['Photography', 'Nature', 'Landscape']:
    li = etree.SubElement(keywords_detail, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    li.text = keyword

# Write the XMP data to a file
xmp_file_path = os.path.join(output_dir, 'example.xmp')  # Corrected variable name here
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(etree.tostring(xmp_root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file saved at {xmp_file_path}")
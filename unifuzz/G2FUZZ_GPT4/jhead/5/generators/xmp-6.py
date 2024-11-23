import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces for XMP
ns_map = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'Iptc4xmpExt': "http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
}

# Create an RDF (Resource Description Framework) structure for the XMP
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=ns_map)

# Create a Description element within the RDF structure
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description')

# Add an example of IPTC character set support for multiple languages
# Here, adding a simple piece of metadata in English and Japanese as an example
dc_title = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}title')
title_bag = etree.SubElement(dc_title, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')
title_en = etree.SubElement(title_bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
title_en.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
title_en.text = 'Example Metadata'
title_jp = etree.SubElement(title_bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
title_jp.set('{http://www.w3.org/XML/1998/namespace}lang', 'ja')
title_jp.text = '例のメタデータ'

# Convert the XML structure to a string
xmp_data = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Save the XMP data to a file
with open('./tmp/example.xmp', 'wb') as file:
    file.write(xmp_data)

print("XMP file generated successfully.")
from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces for XMP
namespaces = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'Iptc4xmpExt': 'http://iptc.org/std/Iptc4xmpExt/2008-02-29/',
    'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
    'xmp': 'http://ns.adobe.com/xap/1.0/',
    'photoshop': 'http://ns.adobe.com/photoshop/1.0/',
    'customNS': 'http://www.example.com/ns/' # Example of a custom namespace
}

# Create an RDF element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=namespaces)

# Create a Description element with multiple properties
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=namespaces)

# Adding title with multiple languages
title = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}title')
title_alt = etree.SubElement(title, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')
etree.SubElement(title_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', lang='en').text = 'Sample Title in English'
etree.SubElement(title_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', lang='fr').text = 'Titre d\'exemple en français'

# Adding creators
creator = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}creator')
creator_seq = etree.SubElement(creator, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq')
etree.SubElement(creator_seq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li').text = 'John Doe'
etree.SubElement(creator_seq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li').text = 'Jane Doe'

# Rights Information
rights = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}rights')
rights_alt = etree.SubElement(rights, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')
etree.SubElement(rights_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', lang='x-default').text = '© 2023 All rights reserved'

# Adding custom metadata
etree.SubElement(description, '{http://www.example.com/ns/}MyCustomField').text = 'Custom Value'

# Photoshop namespace example
etree.SubElement(description, '{http://ns.adobe.com/photoshop/1.0/}Credit').text = 'Photographer Name'

# Wrap everything in an x:xmpmeta element
xmpmeta = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap={'x': 'adobe:ns:meta/'})
xmpmeta.append(rdf)

# Serialize the XML
xml_bytes = etree.tostring(xmpmeta, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write to file
file_path = './tmp/complex_sample.xmp'
with open(file_path, 'wb') as f:
    f.write(xml_bytes)

print(f'XMP file created at {file_path}')
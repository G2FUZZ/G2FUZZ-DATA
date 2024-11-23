from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces for XMP
namespaces = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'Iptc4xmpExt': 'http://iptc.org/std/Iptc4xmpExt/2008-02-29/'
}

# Create an RDF element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=namespaces)

# Create a Description element with multiple language support
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=namespaces)

# Add a title in multiple languages
title = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}title')
title_alt = etree.SubElement(title, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')

# English title
title_en = etree.SubElement(title_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', lang='en')
title_en.text = 'Sample Title in English'

# French title
title_fr = etree.SubElement(title_alt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', lang='fr')
title_fr.text = 'Titre d\'exemple en français'

# Wrap everything in an x:xmpmeta element
xmpmeta = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap={'x': 'adobe:ns:meta/'})
xmpmeta.append(rdf)

# Serialize the XML
xml_bytes = etree.tostring(xmpmeta, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write to file
file_path = './tmp/sample.xmp'
with open(file_path, 'wb') as f:
    f.write(xml_bytes)

print(f'XMP file created at {file_path}')
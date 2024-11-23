import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP metadata to include
metadata = {
    'dc:creator': 'John Doe',
    'dc:rights': '© 2023 John Doe, All rights reserved.',
    'dc:description': 'A sample image with rich metadata',
    'xmpRights:UsageTerms': 'This work is licensed under a Creative Commons Attribution 4.0 International License.',
    'Iptc4xmpExt:LocationShown': 'Earth, Solar System',
    'photoshop:Headline': 'A Journey Through Space',
    'photoshop:Source': 'NASA Imagery',
    'dc:subject': ['Space', 'Earth', 'NASA'],
}

# Create the RDF (Resource Description Framework) structure with corrected namespace usage
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap={
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
    'Iptc4xmpExt': 'http://iptc.org/std/Iptc4xmpExt/2008-02-29/',
    'photoshop': 'http://ns.adobe.com/photoshop/1.0/'
})

# Add metadata to the RDF structure with corrected namespace usage
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap={
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
})

for key, value in metadata.items():
    # Split the key to separate the namespace and tag
    ns, tag = key.split(':', 1)
    # Determine the namespace URL
    ns_url = rdf.nsmap[ns]
    # Create the fully qualified tag name
    qualified_name = f"{{{ns_url}}}{tag}"
    
    if isinstance(value, list):  # For elements with multiple values
        bag = etree.SubElement(description, qualified_name + 'Bag')
        for item in value:
            li = etree.SubElement(bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
            li.text = item
    else:
        element = etree.SubElement(description, qualified_name)
        element.text = value

# Convert the RDF structure to a pretty-printed XML string
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Save the XML to an XMP file
xmp_file_path = './tmp/sample_metadata.xmp'
with open(xmp_file_path, 'wb') as f:
    f.write(xml_bytes)

print(f'Successfully created XMP file at {xmp_file_path}')
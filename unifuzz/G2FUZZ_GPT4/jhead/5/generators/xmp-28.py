import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata information with more complexity
metadata_info = {
    'title': 'Sample Title',
    'description': 'This is a sample description of the XMP file.',
    'creators': ['Creator One', 'Creator Two'],  # List of creators
    'copyrights': {
        'rights': '© 2023 Sample Creator',
        'usageTerms': 'This file may be used under specific conditions.'
    },
    'keywords': ['sample', 'xmp', 'metadata', 'complex']
}

# Namespace definitions
ns_map = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/'
}

# Create the root element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=ns_map)

# Create a description element
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=ns_map)
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')

# Title
title_elem = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}title')
title_elem.text = metadata_info['title']

# Description
description_elem = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}description')
description_elem.text = metadata_info['description']

# Creators (Bag)
creators_elem = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}creator')
creators_bag = etree.SubElement(creators_elem, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')
for creator in metadata_info['creators']:
    li = etree.SubElement(creators_bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    li.text = creator

# Keywords (Seq for ordered list example, can use Bag for unordered)
keywords_elem = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}subject')
keywords_bag = etree.SubElement(keywords_elem, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')
for keyword in metadata_info['keywords']:
    li = etree.SubElement(keywords_bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    li.text = keyword

# Copyrights and Usage Rights
rights_elem = etree.SubElement(description, '{http://ns.adobe.com/xap/1.0/rights/}Rights')
rights_elem.text = metadata_info['copyrights']['rights']

usage_terms_elem = etree.SubElement(description, '{http://ns.adobe.com/xap/1.0/rights/}UsageTerms')
usage_terms_elem.text = metadata_info['copyrights']['usageTerms']

# Convert the XML to a string
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XML to a file
xmp_file_path = './tmp/complex_sample_metadata.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xml_bytes)

print(f"XMP file with complex metadata has been saved to {xmp_file_path}")
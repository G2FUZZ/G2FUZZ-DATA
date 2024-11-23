import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata information with added complexity
metadata_info = {
    'title': 'Advanced Sample Title',
    'description': 'This is an advanced sample description of the XMP file.',
    'creators': [
        {'name': 'Creator One', 'role': 'Author', 'email': 'creator.one@example.com'},
        {'name': 'Creator Two', 'role': 'Contributor', 'email': 'creator.two@example.com'},
    ],
    'copyrights': '© 2023 Advanced Sample Creator',
    'keywords': ['advanced', 'xmp', 'metadata'],
    'customProperties': {
        'ProjectID': '12345',
        'ReviewStatus': 'Approved',
        'Version': '1.0'
    }
}

# Namespace definitions including Dublin Core, Rights Management, and a custom namespace
ns_map = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
    'customNS': 'http://www.example.com/ns#'
}

# Create the root element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=ns_map)

# Create a description element
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=ns_map)
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')

# Adding the title
title_elem = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}title')
title_elem.text = metadata_info['title']

# Adding the description
desc_elem = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}description')
desc_elem.text = metadata_info['description']

# Adding creators with detailed information
creator_seq = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}creator')
creator_bag = etree.SubElement(creator_seq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')

for creator in metadata_info['creators']:
    creator_li = etree.SubElement(creator_bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li', nsmap=ns_map)
    creator_description = etree.SubElement(creator_li, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=ns_map)
    name_elem = etree.SubElement(creator_description, '{http://purl.org/dc/elements/1.1/}creatorName')
    name_elem.text = creator['name']
    role_elem = etree.SubElement(creator_description, '{http://www.example.com/ns#}role')
    role_elem.text = creator['role']
    email_elem = etree.SubElement(creator_description, '{http://www.example.com/ns#}email')
    email_elem.text = creator['email']
    
# Adding copyrights
rights_elem = etree.SubElement(description, '{http://ns.adobe.com/xap/1.0/rights/}UsageTerms')
rights_elem.text = metadata_info['copyrights']

# Adding keywords as a sequence
keywords_seq = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}subject')
keywords_bag = etree.SubElement(keywords_seq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')

for keyword in metadata_info['keywords']:
    keyword_li = etree.SubElement(keywords_bag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    keyword_li.text = keyword

# Adding custom properties
for prop, value in metadata_info['customProperties'].items():
    custom_prop_elem = etree.SubElement(description, f'{{http://www.example.com/ns#}}{prop}')
    custom_prop_elem.text = value

# Convert the XML to a string
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XML to a file
xmp_file_path = './tmp/advanced_sample_metadata_with_complex_structure.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xml_bytes)

print(f"XMP file with advanced metadata and more complex structures has been saved to {xmp_file_path}")
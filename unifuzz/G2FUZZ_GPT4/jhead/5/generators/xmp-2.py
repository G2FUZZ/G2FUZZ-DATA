import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata information
metadata_info = {
    'title': 'Sample Title',
    'description': 'This is a sample description of the XMP file.',
    'creator': 'Sample Creator',
    'copyrights': '© 2023 Sample Creator',
    'keywords': 'sample, xmp, metadata'
}

# Namespace definitions
ns_map = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
}

# Create the root element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=ns_map)

# Create a description element
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap=ns_map)

# Add metadata fields to the description
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')
description.set('{http://purl.org/dc/elements/1.1/}title', metadata_info['title'])
description.set('{http://purl.org/dc/elements/1.1/}description', metadata_info['description'])
description.set('{http://purl.org/dc/elements/1.1/}creator', metadata_info['creator'])
description.set('{http://purl.org/dc/elements/1.1/}rights', metadata_info['copyrights'])
description.set('{http://purl.org/dc/elements/1.1/}subject', metadata_info['keywords'])

# Convert the XML to a string
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XML to a file
xmp_file_path = './tmp/sample_metadata.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xml_bytes)

print(f"XMP file with metadata has been saved to {xmp_file_path}")
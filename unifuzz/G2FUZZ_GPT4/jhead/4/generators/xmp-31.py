import os
from lxml import etree

# Define the namespace map to use in the XMP file
NS_MAP = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmp': 'http://ns.adobe.com/xap/1.0/',
    'xmpMM': 'http://ns.adobe.com/xap/1.0/mm/',
    'pdf': 'http://ns.adobe.com/pdf/1.3/',
    'photoshop': 'http://ns.adobe.com/photoshop/1.0/',
    'prism': 'http://prismstandard.org/namespaces/basic/2.0/',
    'custom': 'http://www.example.com/ns/',
}

# Create the root element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=NS_MAP)

# Create a Description element for document metadata
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description')
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')
description.set('{http://purl.org/dc/elements/1.1/}title', 'Document Title')
description.set('{http://purl.org/dc/elements/1.1/}creator', 'Author Name')
description.set('{http://ns.adobe.com/xap/1.0/}CreateDate', '2023-01-01')
description.set('{http://ns.adobe.com/pdf/1.3/}Producer', 'Producer Name')

# Add custom metadata
customData = etree.SubElement(description, '{http://www.example.com/ns/}customData')
customData.text = 'This is some custom data for the document.'

# Create a History element to track version history
history = etree.SubElement(description, '{http://ns.adobe.com/xap/1.0/mm/}History')
# Version 1
version1 = etree.SubElement(history, '{http://ns.adobe.com/xap/1.0/mm/}StEvt')
version1.set('action', 'created')
version1.set('when', '2023-01-01')
version1.set('softwareAgent', 'Software Agent Name')
# Version 2
version2 = etree.SubElement(history, '{http://ns.adobe.com/xap/1.0/mm/}StEvt')
version2.set('action', 'edited')
version2.set('when', '2023-02-01')
version2.set('softwareAgent', 'Software Agent Name')

# Create a Rights element for document rights information
rights = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}rights')
rights.text = '© 2023 Author Name. All rights reserved.'

# Create directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Write the XMP to a file
xmp_file_path = os.path.join(output_dir, 'complex_document_metadata.xmp')
with open(xmp_file_path, 'wb') as f:
    f.write(b'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
    f.write(etree.tostring(rdf, pretty_print=True))
    f.write(b'\n<?xpacket end="w"?>')

print(f'XMP file with complex document metadata generated at: {xmp_file_path}')
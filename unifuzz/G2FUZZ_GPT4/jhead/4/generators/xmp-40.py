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

# Create a Description element for document metadata with multiple languages
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description')
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')

# Title with multiple languages
titleAlt = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}title')
titleAltBag = etree.SubElement(titleAlt, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt')
for lang, title in [('en', 'Document Title'), ('fr', 'Titre du document')]:
    titleAltLi = etree.SubElement(titleAltBag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    titleAltLi.set('{http://www.w3.org/XML/1998/namespace}lang', lang)
    titleAltLi.text = title

# Creator with multiple entries
creatorSeq = etree.SubElement(description, '{http://purl.org/dc/elements/1.1/}creator')
creatorSeqBag = etree.SubElement(creatorSeq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq')
for creator in ['Author Name', 'Co-author Name']:
    creatorSeqLi = etree.SubElement(creatorSeqBag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    creatorSeqLi.text = creator

# Keywords
keywordsBag = etree.SubElement(description, '{http://ns.adobe.com/photoshop/1.0/}Keywords')
keywordsBagSeq = etree.SubElement(keywordsBag, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag')
for keyword in ['keyword1', 'keyword2', 'keyword3']:
    keywordsLi = etree.SubElement(keywordsBagSeq, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
    keywordsLi.text = keyword

# Structured version history
history = etree.SubElement(description, '{http://ns.adobe.com/xap/1.0/mm/}History')
events = [
    ('created', '2023-01-01', 'Software Agent Name 1', '1.0'),
    ('edited', '2023-02-01', 'Software Agent Name 2', '2.0'),
]
for action, when, agent, version in events:
    stEvt = etree.SubElement(history, '{http://ns.adobe.com/xap/1.0/mm/}StEvt')
    stEvt.set('action', action)
    stEvt.set('when', when)
    stEvt.set('softwareAgent', agent)
    stEvt.set('version', version)

# Create directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Write the XMP to a file
xmp_file_path = os.path.join(output_dir, 'complex_document_metadata_v2.xmp')
with open(xmp_file_path, 'wb') as f:
    f.write(b'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
    f.write(etree.tostring(rdf, pretty_print=True))
    f.write(b'\n<?xpacket end="w"?>')

print(f'XMP file with complex document metadata generated at: {xmp_file_path}')
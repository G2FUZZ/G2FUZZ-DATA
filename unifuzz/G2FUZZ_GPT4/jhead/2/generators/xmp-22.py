import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the root element with increased namespace declarations
xmp_root = Element('xmpmeta')
xmp_root.set('xmlns:x', 'adobe:ns:meta/')
xmp_root.set('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
xmp_root.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
xmp_root.set('xmlns:photoshop', 'http://ns.adobe.com/photoshop/1.0/')
xmp_root.set('xmlns:xmpRights', 'http://ns.adobe.com/xap/1.0/rights/')
xmp_root.set('xmlns:customNS', 'http://www.example.com/ns/')  # Custom namespace

# Add rdf:RDF element
rdf = SubElement(xmp_root, 'rdf:RDF')

# Description element with multiple properties including custom namespace
description = SubElement(rdf, 'rdf:Description', {
    'rdf:about': '',
    'xmlns:xmp': 'http://ns.adobe.com/xap/1.0/',
    'xmlns:customNS': 'http://www.example.com/ns/',
    'xmp:CreatorTool': 'Extended Python Script',
    'xmp:CreateDate': '2023-01-01T12:00:00Z',
    'customNS:Version': '1.0.0'
})

# Adding a complex dc:subject with rdf:Bag
subjects = SubElement(description, 'dc:subject')
subject_bag = SubElement(subjects, 'rdf:Bag')
for subject in ['Tag1', 'Tag2', 'Custom Tag']:
    li = SubElement(subject_bag, 'rdf:li')
    li.text = subject

# Adding multiple languages for dc:description using rdf:Alt
descriptions = SubElement(description, 'dc:description')
description_alt = SubElement(descriptions, 'rdf:Alt')
for lang, text in {'en': 'An advanced example of XMP metadata.', 'fr': 'Un exemple avancé de métadonnées XMP.'}.items():
    li = SubElement(description_alt, 'rdf:li', {'xml:lang': lang})
    li.text = text

# Adding a sequence of creators using rdf:Seq
creators = SubElement(description, 'dc:creator')
creator_seq = SubElement(creators, 'rdf:Seq')
for creator in ['Author One', 'Author Two']:
    li = SubElement(creator_seq, 'rdf:li')
    li.text = creator

# Adding custom structure with nested rdf:Bag for additional metadata
custom_data = SubElement(description, 'customNS:Metadata')
custom_bag = SubElement(custom_data, 'rdf:Bag')
for i, data in enumerate(['Data1', 'Data2', 'Data3'], start=1):
    data_item = SubElement(custom_bag, 'rdf:li')
    data_item.text = f"{data}"

# Convert the created XML structure to a string
raw_xml = tostring(xmp_root, 'utf-8')

# Use parseString to convert the raw XML string to a DOM object, then pretty print it
pretty_xml = parseString(raw_xml).toprettyxml(indent="    ")

# Save the pretty XML to a file
with open('./tmp/extended_complex_metadata.xmp', 'w', encoding='utf-8') as file:
    file.write(pretty_xml)

print("Extended complex XMP file successfully created at './tmp/extended_complex_metadata.xmp'")
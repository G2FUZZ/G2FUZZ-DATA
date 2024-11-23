import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom.minidom import parseString

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the file name
file_name = 'complex_example.xmp'

# XMP basic structure with corrected namespace declarations
xmp_data = Element('x:xmpmeta', {
    'xmlns:x': 'adobe:ns:meta/',
    'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
    'xmlns:xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
    'xmlns:xmp': 'http://ns.adobe.com/xap/1.0/',
    'xmlns:cc': 'http://creativecommons.org/ns#',
    'xmlns:customNS': 'http://example.com/ns#'
})

rdf_RDF = SubElement(xmp_data, 'rdf:RDF')

# Description element with extended licensing, rights management, and creator information
rdf_Description = SubElement(rdf_RDF, 'rdf:Description', {
    'rdf:about': '',
    'xmp:CreatorTool': 'Custom Tool 1.0',
    'xmp:CreateDate': '2023-01-01T12:00:00',
    'customNS:DocumentID': 'unique-document-id-12345'
})

# Creator Information
creator_seq = SubElement(rdf_Description, 'dc:creator')
creator_li = SubElement(creator_seq, 'rdf:Seq')
SubElement(creator_li, 'rdf:li').text = 'Author Name'

# Licensing and Rights Management information, with multiple languages
usage_terms_seq = SubElement(rdf_Description, 'xmpRights:UsageTerms')
usage_terms_li = SubElement(usage_terms_seq, 'rdf:Bag')
SubElement(usage_terms_li, 'rdf:li', {'xml:lang': 'en'}).text = 'This work is licensed under a Creative Commons Attribution 4.0 International License.'
SubElement(usage_terms_li, 'rdf:li', {'xml:lang': 'es'}).text = 'Este trabajo está licenciado bajo la Licencia Internacional Creative Commons Attribution 4.0.'

web_statement = SubElement(rdf_Description, 'xmpRights:WebStatement').text = 'http://creativecommons.org/licenses/by/4.0/'

# Rights in multiple languages
rights_seq = SubElement(rdf_Description, 'dc:rights')
rights_li = SubElement(rights_seq, 'rdf:Bag')
SubElement(rights_li, 'rdf:li', {'xml:lang': 'en'}).text = 'Copyright 2023 by the Author. All rights reserved.'
SubElement(rights_li, 'rdf:li', {'xml:lang': 'es'}).text = 'Derechos de autor 2023 por el Autor. Todos los derechos reservados.'

# Custom Metadata
SubElement(rdf_Description, 'customNS:ExampleField').text = 'Example Value'

# Convert the XML to a byte string
xmp_str = tostring(xmp_data, 'utf-8')

# Pretty printing
dom = parseString(xmp_str)
pretty_xmp_str = dom.toprettyxml(indent='  ')

# Save to file
with open(os.path.join(output_dir, file_name), 'w', encoding='UTF-8') as f:
    f.write(pretty_xmp_str)

print(f'XMP file saved to: {os.path.join(output_dir, file_name)}')
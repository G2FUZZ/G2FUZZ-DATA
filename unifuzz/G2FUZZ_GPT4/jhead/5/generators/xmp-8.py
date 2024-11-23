import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the file name
file_name = 'example.xmp'

# XMP basic structure with corrected namespace declarations
xmp_data = Element('x:xmpmeta', {
    'xmlns:x': 'adobe:ns:meta/',
    'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
})
rdf_RDF = SubElement(xmp_data, 'rdf:RDF')

# Description element with licensing and rights management
rdf_Description = SubElement(rdf_RDF, 'rdf:Description', {
    'rdf:about': '',
    'xmlns:xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
    'xmlns:dc': 'http://purl.org/dc/elements/1.1/'
})

# Licensing and Rights Management information
SubElement(rdf_Description, 'xmpRights:UsageTerms', {'xml:lang': 'en'}).text = 'This work is licensed under a Creative Commons Attribution 4.0 International License.'
SubElement(rdf_Description, 'xmpRights:WebStatement').text = 'http://creativecommons.org/licenses/by/4.0/'
SubElement(rdf_Description, 'dc:rights', {'xml:lang': 'en'}).text = 'Copyright 2023 by the Author. All rights reserved.'

# Convert the XML to a byte string
xmp_str = tostring(xmp_data, 'utf-8')

# Pretty printing
from xml.dom.minidom import parseString
dom = parseString(xmp_str)
pretty_xmp_str = dom.toprettyxml(indent='  ')

# Save to file
with open(os.path.join(output_dir, file_name), 'w', encoding='UTF-8') as f:
    f.write(pretty_xmp_str)

print(f'XMP file saved to: {os.path.join(output_dir, file_name)}')
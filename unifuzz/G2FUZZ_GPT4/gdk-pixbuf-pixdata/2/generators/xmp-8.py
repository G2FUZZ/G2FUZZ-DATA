from lxml import etree as ET

# Define namespaces
ns_map = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xml': 'http://www.w3.org/XML/1998/namespace',  # Added XML namespace
}

# Create root element
rdf = ET.Element(ET.QName(ns_map['rdf'], 'RDF'), nsmap=ns_map)

# Create Description element
description = ET.SubElement(rdf, ET.QName(ns_map['rdf'], 'Description'), {
    ET.QName(ns_map['rdf'], 'about'): '',
    ET.QName(ns_map['dc'], 'title'): '',
})

# Create Alt container for multi-language support
title_alt = ET.SubElement(description, ET.QName(ns_map['dc'], 'title'))
title_alt.set(ET.QName(ns_map['rdf'], 'parseType'), 'Resource')
alt = ET.SubElement(title_alt, ET.QName(ns_map['rdf'], 'Alt'))

# English title
li_en = ET.SubElement(alt, ET.QName(ns_map['rdf'], 'li'), {
    ET.QName(ns_map['xml'], 'lang'): 'en',
})
li_en.text = 'Example Title in English'

# French title
li_fr = ET.SubElement(alt, ET.QName(ns_map['rdf'], 'li'), {
    ET.QName(ns_map['xml'], 'lang'): 'fr',
})
li_fr.text = 'Exemple de titre en français'

# Write to file
xmp_file = './tmp/example_localization.xmp'
tree = ET.ElementTree(rdf)
tree.write(xmp_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

print(f'XMP file with localization support has been created at {xmp_file}')
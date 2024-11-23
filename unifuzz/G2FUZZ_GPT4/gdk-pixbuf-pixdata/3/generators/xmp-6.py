import os
from lxml import etree as ET

# XMP namespace definitions
ns_map = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'x': "adobe:ns:meta/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
    'xml': "http://www.w3.org/XML/1998/namespace"
}

# Create the root element
rdf = ET.Element(ET.QName(ns_map['rdf'], 'RDF'), nsmap=ns_map)

# Description element with about attribute
description = ET.SubElement(rdf, ET.QName(ns_map['rdf'], 'Description'), nsmap=ns_map)
description.set(ET.QName(ns_map['rdf'], 'about'), '')

# Title element (default language)
title = ET.SubElement(description, ET.QName(ns_map['dc'], 'title'))
alt = ET.SubElement(title, ET.QName(ns_map['rdf'], 'Alt'))
li_en = ET.SubElement(alt, ET.QName(ns_map['rdf'], 'li'), {'{http://www.w3.org/XML/1998/namespace}lang': 'x-default'})
li_en.text = "Sample XMP Metadata in multiple languages"

# Adding French title
li_fr = ET.SubElement(alt, ET.QName(ns_map['rdf'], 'li'), {'{http://www.w3.org/XML/1998/namespace}lang': 'fr'})
li_fr.text = "Exemple de métadonnées XMP dans plusieurs langues"

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Write the XMP file
xmp_file_path = './tmp/multilanguage_metadata.xmp'
with open(xmp_file_path, 'wb') as f:
    f.write(b'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
    f.write(ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
    f.write(b'\n<?xpacket end="w"?>')

print(f"XMP file with internationalization and localization support created at: {xmp_file_path}")
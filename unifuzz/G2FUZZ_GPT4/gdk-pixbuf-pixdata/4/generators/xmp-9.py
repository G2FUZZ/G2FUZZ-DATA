from lxml import etree as ET

# Define namespaces for XMP
namespaces = {
    'x': "adobe:ns:meta/",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/"
}

# Create the base XML structure
rdf = ET.Element(ET.QName(namespaces['rdf'], 'RDF'), nsmap=namespaces)

# Create a Description element for licensing and rights management
description = ET.SubElement(rdf, ET.QName(namespaces['rdf'], 'Description'), nsmap=namespaces)
description.set(ET.QName(namespaces['rdf'], 'about'), '')

# Add licensing information
license = ET.SubElement(description, ET.QName(namespaces['xmpRights'], 'UsageTerms'))
license_lang = ET.SubElement(license, ET.QName(namespaces['rdf'], 'Alt'))
li = ET.SubElement(license_lang, ET.QName(namespaces['rdf'], 'li'))
li.set('{http://www.w3.org/XML/1998/namespace}lang', 'x-default')
li.text = 'This work is licensed under the Creative Commons Attribution 4.0 International License.'

# Add rights management information
rights = ET.SubElement(description, ET.QName(namespaces['xmpRights'], 'Marked'))
rights.text = 'True'

# Create and write the XMP file
xmp_tree = ET.ElementTree(rdf)
xmp_file_path = './tmp/licensing_rights_management.xmp'
xmp_tree.write(xmp_file_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

print(f'XMP file generated and saved to {xmp_file_path}')
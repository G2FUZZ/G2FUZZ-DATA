from lxml import etree as ET

# Define namespaces for the standard and custom fields
namespaces = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/",
    'custom': "http://www.yourdomain.com/xmp/custom/",
    'anotherCustom': "http://www.anotherdomain.com/xmp/custom/"
}

# Create root element
rdf = ET.Element(ET.QName(namespaces['rdf'], 'RDF'), nsmap=namespaces)

# Create a Description element for Dublin Core standard fields
description_dc = ET.SubElement(rdf, ET.QName(namespaces['rdf'], 'Description'), nsmap=namespaces)

# Add standard metadata fields from Dublin Core (e.g., title, creator)
dc_title = ET.SubElement(description_dc, ET.QName(namespaces['dc'], 'title'))
dc_title.text = 'Example Document Title'

dc_creator = ET.SubElement(description_dc, ET.QName(namespaces['dc'], 'creator'))
dc_creator_seq = ET.SubElement(dc_creator, ET.QName(namespaces['rdf'], 'Seq'))
dc_creator_li = ET.SubElement(dc_creator_seq, ET.QName(namespaces['rdf'], 'li'))
dc_creator_li.text = 'Author Name'

# Add rights information
rights_description = ET.SubElement(description_dc, ET.QName(namespaces['xmpRights'], 'UsageTerms'))
rights_description_seq = ET.SubElement(rights_description, ET.QName(namespaces['rdf'], 'Alt'))
rights_description_li = ET.SubElement(rights_description_seq, ET.QName(namespaces['rdf'], 'li'), attrib={ET.QName(namespaces['rdf'], 'lang'): 'x-default'})
rights_description_li.text = '© 2023. All rights reserved.'

# Create another Description element for custom fields
description_custom = ET.SubElement(rdf, ET.QName(namespaces['rdf'], 'Description'), nsmap=namespaces)

# Add a custom metadata field
custom_field = ET.SubElement(description_custom, ET.QName(namespaces['custom'], 'CustomField'))
custom_field.text = 'Custom metadata value'

# Add another set of custom metadata in a different namespace
description_anotherCustom = ET.SubElement(rdf, ET.QName(namespaces['rdf'], 'Description'), nsmap=namespaces)
another_custom_field = ET.SubElement(description_anotherCustom, ET.QName(namespaces['anotherCustom'], 'AnotherCustomField'))
another_custom_field.text = 'Another custom metadata value'

# Generate the complete XML tree
tree = ET.ElementTree(rdf)
# Ensure the './tmp/' directory exists or adjust the path as needed
output_path = './tmp/complex_example_metadata.xmp'
tree.write(output_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

print(f"XMP file saved to {output_path}")
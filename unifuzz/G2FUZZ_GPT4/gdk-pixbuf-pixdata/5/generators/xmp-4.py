from lxml import etree as ET

# Define namespaces for the standard fields
namespaces = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
    # Add more namespaces for other standard fields as needed
    'custom': "http://www.yourdomain.com/xmp/custom/"
}

# Create root element
rdf = ET.Element(ET.QName(namespaces['rdf'], 'RDF'), nsmap=namespaces)

# Create a Description element for Dublin Core standard fields
description_dc = ET.SubElement(rdf, ET.QName(namespaces['rdf'], 'Description'), nsmap=namespaces)

# Add standard metadata fields from Dublin Core (e.g., title)
dc_title = ET.SubElement(description_dc, ET.QName(namespaces['dc'], 'title'))
dc_title.text = 'Example Document Title'

# Create another Description element for custom fields
description_custom = ET.SubElement(rdf, ET.QName(namespaces['rdf'], 'Description'), nsmap=namespaces)

# Add a custom metadata field
custom_field = ET.SubElement(description_custom, ET.QName(namespaces['custom'], 'CustomField'))
custom_field.text = 'Custom metadata value'

# Generate the complete XML tree
tree = ET.ElementTree(rdf)
# Ensure the './tmp/' directory exists or adjust the path as needed
output_path = './tmp/example_metadata.xmp'
tree.write(output_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

print(f"XMP file saved to {output_path}")
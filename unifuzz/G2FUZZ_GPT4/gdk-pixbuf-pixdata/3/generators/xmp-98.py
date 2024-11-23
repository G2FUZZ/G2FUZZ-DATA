from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Base namespaces
namespaces = {
    "x": "adobe:ns:meta/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "xmpRights": "http://ns.adobe.com/xap/1.0/rights/",
    "cc": "http://creativecommons.org/ns#",
    "photoshop": "http://ns.adobe.com/photoshop/1.0/",
    "tiff": "http://ns.adobe.com/tiff/1.0/",
    "exif": "http://ns.adobe.com/exif/1.0/",
    "customNS": "http://example.com/ns#"  # Custom namespace
}

# Define the root of the XMP data
xmpmeta = etree.Element("{adobe:ns:meta/}xmpmeta", nsmap=namespaces)
rdf = etree.SubElement(xmpmeta, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF")
description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", attrib={
    "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about": "",
    "{http://example.com/ns#}feature": "Example Feature",  # Corrected custom attribute
})

# Dynamically adding multiple creators
creators = ["Jane Doe", "John Smith"]
creator_seq = etree.SubElement(description, "{http://purl.org/dc/elements/1.1/}creator")
creator_bag = etree.SubElement(creator_seq, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")

for creator in creators:
    creator_item = etree.SubElement(creator_bag, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
    creator_item.text = creator

# Condition-based metadata
include_additional_info = True
if include_additional_info:
    custom_property = etree.SubElement(description, "{http://example.com/ns#}additionalProperty")
    custom_property.text = "Additional information based on condition"

# Writing to file
xmp_file_path = './tmp/complex_dynamic.xmp'
with open(xmp_file_path, 'wb') as f:
    f.write(etree.tostring(xmpmeta, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file with complex metadata saved to {xmp_file_path}")
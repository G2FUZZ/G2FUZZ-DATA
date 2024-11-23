from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata
metadata = {
    "title": "Sample Image",
    "description": "This is a sample image used for demonstrating XMP metadata capabilities.",
    "creator": "John Doe",
    "license": "Creative Commons Attribution 4.0 International",
    "rightsManagement": "This image is free to use under Creative Commons Attribution 4.0 International License",
}

# Define namespaces
ns_map = {
    'x': "adobe:ns:meta/",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/",
}

# Create an XML structure for the XMP file using the defined namespaces
xmp_data = etree.Element("{%s}xmpmeta" % ns_map['x'], nsmap={'x': ns_map['x']})
rdf = etree.SubElement(xmp_data, "{%s}RDF" % ns_map['rdf'], nsmap={'rdf': ns_map['rdf']})
description = etree.SubElement(
    rdf, 
    "{%s}Description" % ns_map['rdf'], 
    nsmap={'dc': ns_map['dc'], 'xmpRights': ns_map['xmpRights']},
    **{
        "{%s}title" % ns_map['dc']: metadata["title"],
        "{%s}description" % ns_map['dc']: metadata["description"],
        "{%s}creator" % ns_map['dc']: metadata["creator"],
        "{%s}UsageTerms" % ns_map['xmpRights']: metadata["rightsManagement"],
        "{%s}License" % ns_map['xmpRights']: metadata["license"]
    }
)

# Convert the XML structure to a byte string
xmp_bytes = etree.tostring(xmp_data, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/sample_image_metadata.xmp'
with open(xmp_file_path, 'wb') as file:
    file.write(xmp_bytes)

print(f"XMP file saved to {xmp_file_path}")
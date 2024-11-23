import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Base namespaces
namespaces = {
    'x': "adobe:ns:meta/",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/"
}

# Metadata information
metadata_info = {
    'descriptions': [
        "Feature 1: Detailed explanation of feature 1.",
        "Feature 2: Detailed explanation of feature 2."
    ],
    'creator': ["John Doe", "Jane Doe"],
    'rights': "© 2023 Creator. All rights reserved."
}

# Function to create RDF Description
def create_rdf_description(parent, tag, namespace, values):
    desc_elem = SubElement(parent, f"{{{namespaces['rdf']}}}Description")
    for value in values:
        child_elem = SubElement(desc_elem, f"{{{namespaces[namespace]}}}{tag}")
        child_elem.text = value

# Create XMP content
root = Element(f"{{{namespaces['x']}}}xmpmeta")
rdf = SubElement(root, f"{{{namespaces['rdf']}}}RDF")

# Descriptions
create_rdf_description(rdf, 'description', 'dc', metadata_info['descriptions'])

# Creator
create_rdf_description(rdf, 'creator', 'dc', metadata_info['creator'])

# Rights
create_rdf_description(rdf, 'Rights', 'xmpRights', [metadata_info['rights']])

# Convert to string
raw_str = tostring(root, 'utf-8')
pretty_str = parseString(raw_str).toprettyxml(indent="   ")

# Wrap with xpacket
xmp_content = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
{pretty_str}
<?xpacket end="w"?>"""

# Path to the XMP file to be created
xmp_file_path = './tmp/complex_feature_description.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f"XMP file created at {xmp_file_path}")
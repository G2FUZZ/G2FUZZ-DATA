from lxml import etree
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define namespaces to be used
ns_map = {
    'x': "adobe:ns:meta/",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/"
}

# Define the root of the XMP data with the correct namespace
root = etree.Element("{adobe:ns:meta/}xmpmeta", nsmap={'x': ns_map['x']})
rdf = etree.SubElement(root, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap={'rdf': ns_map['rdf']})

# Define a basic structure for the Description within an RDF element
description = etree.SubElement(
    rdf,
    "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description",
    {
        "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about": ""
    },
    nsmap={'dc': ns_map['dc']}  # Declare the DC namespace here
)

# Adding the feature description as a dc:description
feature_description = """
2. **Extensibility**: The XMP framework supports adding custom metadata fields on top of the existing standard ones. 
This makes it highly adaptable to different domains and user needs, allowing for the storage of specialized information.
"""
description_elem = etree.SubElement(description, "{http://purl.org/dc/elements/1.1/}description")
description_elem.text = etree.CDATA(feature_description)

# Convert the XML structure to a byte string
xmp_data = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")

# Define the output file path
output_file_path = os.path.join(output_dir, "features.xmp")

# Write the XMP data to the file
with open(output_file_path, "wb") as f:
    f.write(xmp_data)

print(f"XMP file saved at: {output_file_path}")
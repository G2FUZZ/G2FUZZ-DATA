import os
from lxml import etree

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define namespaces to be used in the XMP file
namespaces = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xmp": "http://ns.adobe.com/xap/1.0/",
    "custom": "http://my.namespace.com/custom/1.0/"
}

# Create an RDF (Resource Description Framework) structure for the XMP data
rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with custom namespace and properties
description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")
description.set("{http://my.namespace.com/custom/1.0/}Feature", "Extensibility")
description.set("{http://my.namespace.com/custom/1.0/}Description", "XMP supports adding custom namespaces and properties, which allows for the inclusion of any type of metadata. This means that as new types of metadata are needed, they can be added without affecting existing data.")

# Convert the constructed XML into a string
xmp_data = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding="UTF-8")

# Write the XMP data to a file
xmp_file_path = os.path.join(output_dir, "example.xmp")
with open(xmp_file_path, "wb") as xmp_file:
    xmp_file.write(xmp_data)

print(f"XMP file has been successfully created at {xmp_file_path}")
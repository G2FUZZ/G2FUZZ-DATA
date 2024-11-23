import os
from xml.etree.ElementTree import Element, SubElement, tostring, QName
from xml.dom.minidom import parseString

def prettify(elem):
    """Return a pretty-printed XML string for the element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Namespace URIs
ns_x = "adobe:ns:meta/"
ns_rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
ns_dc = "http://purl.org/dc/elements/1.1/"
custom_ns = "http://my.custom.namespace/"

# Register namespaces and create QName objects for tags
xmpmeta_qname = QName(ns_x, 'xmpmeta')
rdf_qname = QName(ns_rdf, 'RDF')
description_qname = QName(ns_rdf, 'Description')
dc_description_qname = QName(ns_dc, 'description')

# The base structure of the XMP data
xmp_base = Element(xmpmeta_qname, {'xmlns:x': ns_x})
rdf = SubElement(xmp_base, rdf_qname, {'xmlns:rdf': ns_rdf})

# A more complex example involving multiple descriptions and custom namespaces
description1 = SubElement(rdf, description_qname, {'rdf:about': "", 'xmlns:dc': ns_dc})
dc_description = SubElement(description1, dc_description_qname)
dc_description.text = "An example of a complex XMP file."

# Adding a custom namespace and properties
description2 = SubElement(rdf, description_qname, {'rdf:about': "", 'xmlns:my_ns': custom_ns})
custom_property = SubElement(description2, QName(custom_ns, 'customProperty'))
custom_property.text = "Custom property value"

# Nested structures example
nested_description = SubElement(description2, QName(custom_ns, 'nestedProperty'))
nested_value = SubElement(nested_description, QName(custom_ns, 'value'))
nested_value.text = "Nested property value"

xmp_content = prettify(xmp_base)

# Directory to save the XMP file
output_dir = "./tmp/"
# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# The name of the XMP file
xmp_filename = "complex_feature_description.xmp"

# Full path for the XMP file
xmp_file_path = os.path.join(output_dir, xmp_filename)

# Writing the content to the XMP file
with open(xmp_file_path, "w") as file:
    file.write(xmp_content)

print(f"XMP file saved to: {xmp_file_path}")
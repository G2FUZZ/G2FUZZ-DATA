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
custom_ns1 = "http://my.custom.namespace1/"
custom_ns2 = "http://my.custom.namespace2/"

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
dc_description.text = "An example of a complex XMP file with richer metadata."

# Adding custom namespaces and properties
description2 = SubElement(rdf, description_qname, {'rdf:about': "", 'xmlns:ns1': custom_ns1, 'xmlns:ns2': custom_ns2})

# Custom property from namespace 1
custom_property1 = SubElement(description2, QName(custom_ns1, 'customProperty1'))
custom_property1.text = "Custom property value from namespace 1"

# Custom property from namespace 2
custom_property2 = SubElement(description2, QName(custom_ns2, 'customProperty2'))
custom_property2.text = "Custom property value from namespace 2"

# Adding array properties (Seq for ordered elements, Bag for unordered)
seq_property = SubElement(description2, QName(ns_rdf, 'Seq'), {QName(ns_rdf, 'about'): "SequenceExample"})
for i in range(1, 4):
    li = SubElement(seq_property, QName(ns_rdf, 'li'))
    li.text = f"Ordered item {i}"

bag_property = SubElement(description2, QName(ns_rdf, 'Bag'), {QName(ns_rdf, 'about'): "BagExample"})
for i in range(1, 4):
    li = SubElement(bag_property, QName(ns_rdf, 'li'))
    li.text = f"Unordered item {i}"

# Structured property example
structured_property = SubElement(description2, QName(custom_ns2, 'StructuredProperty'))
part1 = SubElement(structured_property, QName(custom_ns2, 'Part1'))
part1.text = "First part of the structure"
part2 = SubElement(structured_property, QName(custom_ns2, 'Part2'))
part2.text = "Second part of the structure"

xmp_content = prettify(xmp_base)

# Directory to save the XMP file
output_dir = "./tmp/"
# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# The name of the XMP file
xmp_filename = "more_complex_feature_description.xmp"

# Full path for the XMP file
xmp_file_path = os.path.join(output_dir, xmp_filename)

# Writing the content to the XMP file
with open(xmp_file_path, "w") as file:
    file.write(xmp_content)

print(f"XMP file saved to: {xmp_file_path}")
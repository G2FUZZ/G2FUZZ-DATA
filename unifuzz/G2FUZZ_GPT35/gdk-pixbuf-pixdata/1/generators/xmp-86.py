import os
from lxml import etree

# Create a function to generate XMP files with complex structures
def generate_complex_xmp_file(file_name):
    xmp_root = etree.Element("xmpmeta", xmlns="adobe:ns:meta/", xmlns_x="adobe:ns:meta/xmp/", x="adobe:ns:meta/xmp/", ns_property="http://example.com/ns/property/")

    rdf_description = etree.SubElement(xmp_root, "RDF")
    description = etree.SubElement(rdf_description, "Description")

    # Add metadata information
    author = etree.SubElement(description, "{http://example.com/ns/property/}creator", ns_property="http://example.com/ns/property/")
    author.text = "Jane Smith"

    copyright = etree.SubElement(description, "{http://example.com/ns/property/}rights", ns_property="http://example.com/ns/property/")
    copyright.text = "All rights reserved"

    # Add nested elements
    nested_element = etree.SubElement(description, "{http://example.com/ns/property/}nestedElement", ns_property="http://example.com/ns/property/")
    nested_sub_element = etree.SubElement(nested_element, "{http://example.com/ns/property/}subElement", ns_property="http://example.com/ns/property/")
    nested_sub_element.text = "Nested Element Value"

    # Add attributes to elements
    nested_element.set("attribute1", "value1")
    nested_sub_element.set("attribute2", "value2")

    # Create the XMP file
    xmp_str = etree.tostring(xmp_root, pretty_print=True, encoding='utf-8', xml_declaration=True)
    with open(f"./tmp/{file_name}.xmp", "wb") as xmp_file:
        xmp_file.write(xmp_str)

# Generate XMP files with complex structures
generate_complex_xmp_file("complex_sample_file")
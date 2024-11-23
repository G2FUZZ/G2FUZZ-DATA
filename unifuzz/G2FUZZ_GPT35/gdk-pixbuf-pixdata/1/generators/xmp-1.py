import os
from lxml import etree

# Create a function to generate XMP files
def generate_xmp_file(file_name):
    xmp_root = etree.Element("xmpmeta", xmlns="adobe:ns:meta/", xmlns_x="adobe:ns:meta/xmp/", x="adobe:ns:meta/xmp/")

    rdf_description = etree.SubElement(xmp_root, "RDF")
    description = etree.SubElement(rdf_description, "Description")

    # Add metadata information
    author = etree.SubElement(description, "creator")
    author.text = "John Doe"

    copyright = etree.SubElement(description, "rights")
    copyright.text = "Copyright 2021"

    keywords = etree.SubElement(description, "subject")
    keywords.text = "Python, XMP, Metadata"

    creation_date = etree.SubElement(description, "CreateDate")
    creation_date.text = "2021-09-30"

    # Create the XMP file
    xmp_str = etree.tostring(xmp_root, pretty_print=True, encoding='utf-8', xml_declaration=True)
    with open(f"./tmp/{file_name}.xmp", "wb") as xmp_file:
        xmp_file.write(xmp_str)

# Generate XMP files
generate_xmp_file("sample_file_1")
generate_xmp_file("sample_file_2")
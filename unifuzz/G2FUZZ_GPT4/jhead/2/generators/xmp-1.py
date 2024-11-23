import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an XMP file with extendibility feature
def create_xmp_file(filename: str):
    # Define namespaces
    rdf_ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmp_ns = "http://ns.adobe.com/xap/1.0/"

    # Create root element
    rdf = Element(f"{{{rdf_ns}}}RDF")
    rdf.set("xmlns:rdf", rdf_ns)
    rdf.set("xmlns:xmp", xmp_ns)

    # Create Description element
    description = SubElement(rdf, f"{{{rdf_ns}}}Description")
    description.set(f"{{{rdf_ns}}}about", "")
    description.set("xmlns:xmp", xmp_ns)

    # Add a custom metadata field to demonstrate extendibility
    custom_field = SubElement(description, "xmp:CustomField")
    custom_field.text = "This is a custom metadata field to demonstrate extendibility."

    # Convert to string and write to file
    tree = ElementTree(rdf)
    with open(os.path.join(output_dir, filename), "wb") as file:
        tree.write(file, xml_declaration=True, encoding='utf-8')

# Example usage
create_xmp_file("example_extendibility.xmp")
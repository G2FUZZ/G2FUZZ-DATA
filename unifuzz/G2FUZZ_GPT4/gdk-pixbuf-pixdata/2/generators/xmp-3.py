import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree, register_namespace

# Create the directory for storing the files if it does not already exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the content to be included in the XMP file
content = "3. **Extensibility**: XMP is built on XML, making it highly extensible. Users can define custom metadata schemas according to their needs, in addition to using predefined schemas such as Dublin Core, Exif, or IPTC."

# Register namespaces to avoid the 'unbound prefix' error
register_namespace('x', "adobe:ns:meta/")
register_namespace('rdf', "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
register_namespace('dc', "http://purl.org/dc/elements/1.1/")

# Create an XML structure for the XMP file
xmp_root = Element("{adobe:ns:meta/}xmpmeta")
rdf_RDF = SubElement(xmp_root, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF")

rdf_Description = SubElement(rdf_RDF, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", {
    "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about": ""
})

# Insert the content as a description under the Dublin Core namespace
dc_description = SubElement(rdf_Description, "{http://purl.org/dc/elements/1.1/}description")
dc_description.text = content

# Convert the ElementTree to a string
xmp_data = tostring(xmp_root, 'utf-8')

# Pretty printing XML for readability
from xml.dom.minidom import parseString
dom = parseString(xmp_data)
pretty_xmp_data = dom.toprettyxml(indent="   ")

# Define the file name and path
file_name = "example.xmp"
file_path = os.path.join(output_dir, file_name)

# Write the pretty printed XMP data to a file
with open(file_path, "w") as file:
    file.write(pretty_xmp_data)

print(f"XMP file '{file_name}' has been created in '{output_dir}'.")
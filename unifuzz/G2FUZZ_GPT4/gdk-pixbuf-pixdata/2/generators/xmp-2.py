import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# XMP data to include
xmp_data = """
2. **Interoperability**: Designed to work across different media types, XMP supports a wide range of file formats including PDF, JPEG, GIF, PNG, TIFF, MP3, and many types of RAW image files. This interoperability ensures that metadata is preserved and accessible regardless of the software or platform used.
"""

# Define namespaces
NSMAP = {
    'x': 'adobe:ns:meta/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/'  # Added 'dc' namespace here
}

# Create an XML structure for the XMP file using the defined namespaces
xmp_root = ET.Element("{%s}xmpmeta" % NSMAP['x'], nsmap={'x': NSMAP['x']})  # Specify nsmap for this element
rdf_RDF = ET.SubElement(xmp_root, "{%s}RDF" % NSMAP['rdf'], nsmap={'rdf': NSMAP['rdf']})

rdf_Description = ET.SubElement(rdf_RDF, "{%s}Description" % NSMAP['rdf'], {
    "{%s}about" % NSMAP['rdf']: ""
}, nsmap={'dc': NSMAP['dc']})  # 'dc' namespace is now part of the nsmap for rdf_Description

dc_format = ET.SubElement(rdf_Description, "{%s}format" % NSMAP['dc'])
dc_format.text = "application/xmp"

dc_description = ET.SubElement(rdf_Description, "{%s}description" % NSMAP['dc'])
dc_description.text = xmp_data

# Convert the XML to a byte string
xmp_bytes = ET.tostring(xmp_root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# File path where to save the XMP file
file_path = os.path.join(output_dir, "metadata.xmp")

# Write the XMP data to a file
with open(file_path, "wb") as file:
    file.write(xmp_bytes)
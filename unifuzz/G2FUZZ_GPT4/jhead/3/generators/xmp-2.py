import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Define the base directory to save the XMP files
base_dir = './tmp/'

# Ensure the base directory exists
os.makedirs(base_dir, exist_ok=True)

# Define the XMP file content using ElementTree for XML creation
xmp_data = Element('x:xmpmeta', xmlns='adobe:ns:meta/')
rdf = SubElement(xmp_data, 'rdf:RDF', xmlns='http://www.w3.org/1999/02/22-rdf-syntax-ns#')

# Add description about the extensibility feature
description = SubElement(rdf, 'rdf:Description', xmlns='http://purl.org/dc/elements/1.1/')
extensibility = SubElement(description, 'dc:description')
extensibility.text = "Users can define their own sets of metadata fields, making XMP highly adaptable to different needs and industries, including photography, design, publishing, and more."

# Convert to a proper XML string
xml_data = tostring(xmp_data, 'utf-8')

# Write to a file
file_path = os.path.join(base_dir, 'extensibility_feature.xmp')
with open(file_path, 'wb') as file:
    file.write(xml_data)

print(f"XMP file created at {file_path}")
import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument here

# Define namespaces for XMP
namespaces = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmp': "http://ns.adobe.com/xap/1.0/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with accessibility features
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Adding detailed descriptions and keywords for accessibility
dc_description = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}description")
dc_description.text = "A detailed description of the content, enhancing accessibility by providing context that can be read by screen readers."

dc_keywords = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}subject")
rdf_Bag = ET.SubElement(dc_keywords, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag")
for keyword in ['Accessibility', 'Screen Reader', 'Detailed Description']:
    rdf_li = ET.SubElement(rdf_Bag, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
    rdf_li.text = keyword

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/accessibility_features.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"XMP file with accessibility features created at: {xmp_file_path}")
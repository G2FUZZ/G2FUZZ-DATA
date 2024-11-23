from lxml import etree as ET

# Define the XMP namespaces required for localization
ns_map = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "xmp": "http://ns.adobe.com/xap/1.0/",
    "xml": "http://www.w3.org/XML/1998/namespace"
}

# Create the root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=ns_map)

# Create a Description element with localized titles
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description",
                            attrib={"{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about": ""})

# Title element with multiple language support
title = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}title")

# Alt element for alternative languages
alt = ET.SubElement(title, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt")

# English title
en_title = ET.SubElement(alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li",
                         attrib={"{http://www.w3.org/XML/1998/namespace}lang": "en"})
en_title.text = "Sample Title in English"

# French title
fr_title = ET.SubElement(alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li",
                         attrib={"{http://www.w3.org/XML/1998/namespace}lang": "fr"})
fr_content = "Titre d'exemple en français"
fr_title.text = fr_content

# Generate pretty printed string of the XML
xml_str = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode()

# Define the path for the output XMP file
output_path = './tmp/localized_metadata.xmp'

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists(os.path.dirname(output_path)):
    os.makedirs(os.path.dirname(output_path))

# Write the XMP data to the file
with open(output_path, "w", encoding="utf-8") as file:
    file.write(xml_str)

print(f"XMP file with localization features has been saved to {output_path}")
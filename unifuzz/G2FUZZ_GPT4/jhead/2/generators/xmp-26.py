import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces including additional ones for Rights, Media Management, and a custom namespace
namespaces = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/",
    'xmpMM': "http://ns.adobe.com/xap/1.0/mm/",
    'ex': "http://example.com/ns/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with accessibility features and more
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Adding detailed descriptions and keywords for accessibility
dc_description = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}description")
dc_description.text = "A detailed description including accessibility, rights, and media management."

dc_keywords = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}subject")
rdf_Bag = ET.SubElement(dc_keywords, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag")
for keyword in ['Accessibility', 'Rights Management', 'Media Management']:
    rdf_li = ET.SubElement(rdf_Bag, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
    rdf_li.text = keyword

# Rights Management Information
rights_UsageTerms = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/rights/}UsageTerms")
rights_UsageTerms.text = "This content is protected by copyright laws and is provided for authorized use only."

# Media Management - Instance ID and Original Document ID
xmpMM_InstanceID = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}InstanceID")
xmpMM_InstanceID.text = "uuid:12345678-1234-1234-1234-123456789012"

xmpMM_OriginalDocumentID = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}OriginalDocumentID")
xmpMM_OriginalDocumentID.text = "uuid:abcd1234-abcd-1234-abcd-abcd1234abcd"

# Custom Extension for Example Metadata
ex_CustomData = ET.SubElement(description, "{http://example.com/ns/}CustomData")
ex_CustomData.text = "This is custom data for demonstration purposes."

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/complex_accessibility_features.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"Complex XMP file with additional structures created at: {xmp_file_path}")
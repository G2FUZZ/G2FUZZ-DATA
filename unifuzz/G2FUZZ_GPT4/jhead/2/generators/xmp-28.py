import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces including additional ones for Rights, Media Management, and a custom namespace with extensions
namespaces = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/",
    'xmpMM': "http://ns.adobe.com/xap/1.0/mm/",
    'xmpGImg': "http://ns.adobe.com/xap/1.0/g/img/",
    'ex': "http://example.com/ns/",
    'cc': "http://creativecommons.org/ns#",
    'xmpDM': "http://ns.adobe.com/xmp/1.0/DynamicMedia/",
    'exComplex': "http://example.com/ns/complex/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with accessibility features and more
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Insert additional metadata here as needed
# For example, adding a complex structured type for a custom namespace

# Custom Complex Data with Nested Elements
ex_ComplexData = ET.SubElement(description, "{http://example.com/ns/complex/}ComplexData")

# Adding a nested structured element with attributes
ex_StructuredData = ET.SubElement(ex_ComplexData, "{http://example.com/ns/complex/}StructuredData")
ex_StructuredData.set("attribute", "Value")
ex_StructuredData.text = "This is structured data with attributes and nested elements."

# Adding a sequence of complex types
ex_Sequence = ET.SubElement(ex_ComplexData, "{http://example.com/ns/complex/}Sequence")
for i in range(3):
    ex_Item = ET.SubElement(ex_Sequence, "{http://example.com/ns/complex/}Item")
    ex_Item.set("id", str(i))
    ex_Item.text = f"Item {i} in the sequence"

# Multilingual fields using RDF Alt for different languages
ex_MultilingualField = ET.SubElement(ex_ComplexData, "{http://example.com/ns/complex/}MultilingualField")
rdf_Alt = ET.SubElement(ex_MultilingualField, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt")
for lang, text in [("en", "English Text"), ("fr", "Texte Français"), ("es", "Texto en Español")]:
    rdf_li = ET.SubElement(rdf_Alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li", {"{http://www.w3.org/XML/1998/namespace}lang": lang})
    rdf_li.text = text

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/extended_complex_accessibility_features.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"Extended complex XMP file with additional structures created at: {xmp_file_path}")
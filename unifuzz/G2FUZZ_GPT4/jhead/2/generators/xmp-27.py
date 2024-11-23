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
    'xmpGImg': "http://ns.adobe.com/xap/1.0/g/img/",
    'ex': "http://example.com/ns/",
    'cc': "http://creativecommons.org/ns#",
    'xmpDM': "http://ns.adobe.com/xmp/1.0/DynamicMedia/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with accessibility features and more
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Adding detailed descriptions in multiple languages
dc_description_en = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}description", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
dc_description_en.text = "An English detailed description including accessibility, rights, and media management."

dc_description_fr = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}description", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"})
dc_description_fr.text = "Une description détaillée en français incluant l'accessibilité, la gestion des droits et la gestion des médias."

# Adding keywords with structured properties
dc_subjects = ET.SubElement(description, "{http://purl.org/dc/elements/1.1/}subject")
rdf_Bag_subjects = ET.SubElement(dc_subjects, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag")
for keyword in ['Accessibility', 'Rights Management', 'Media Management']:
    rdf_li = ET.SubElement(rdf_Bag_subjects, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
    rdf_li.text = keyword

# Rights and Usage structured information
rights_UsageTerms = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/rights/}UsageTerms")
rdf_Alt = ET.SubElement(rights_UsageTerms, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt")
rdf_li_en = ET.SubElement(rdf_Alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
rdf_li_en.text = "This content is protected by copyright laws and is provided for authorized use only."
rdf_li_fr = ET.SubElement(rdf_Alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"})
rdf_li_fr.text = "Ce contenu est protégé par les lois sur le droit d'auteur et est fourni uniquement pour une utilisation autorisée."

# Media Management - Detailed Instance ID, Original Document ID, and Manifestation
xmpMM_InstanceID = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}InstanceID")
xmpMM_InstanceID.text = "uuid:12345678-1234-1234-1234-123456789012"

xmpMM_OriginalDocumentID = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}OriginalDocumentID")
xmpMM_OriginalDocumentID.text = "uuid:abcd1234-abcd-1234-abcd-abcd1234abcd"

# Creator Contact Information
xmpCreators = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}Creators")
rdf_Seq = ET.SubElement(xmpCreators, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
rdf_li_creator1 = ET.SubElement(rdf_Seq, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
rdf_li_creator1.text = "John Doe"
rdf_li_creator2 = ET.SubElement(rdf_Seq, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
rdf_li_creator2.text = "Jane Smith"

# Custom Extension for Example Metadata
ex_CustomData = ET.SubElement(description, "{http://example.com/ns/}CustomData")
ex_CustomData.text = "This is custom data for demonstration purposes, including complex structured information."

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/complex_accessibility_features.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"Complex XMP file with additional structures created at: {xmp_file_path}")
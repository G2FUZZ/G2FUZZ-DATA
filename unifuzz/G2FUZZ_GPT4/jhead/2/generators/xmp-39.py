import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces including additional ones for more complex structures
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
    'exStruct': "http://example.com/ns/structured/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with more complex structures
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Adding a complex structure for Topics with nested structured properties
topics = ET.SubElement(description, "{http://example.com/ns/}Topics")
rdf_Bag_topics = ET.SubElement(topics, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag")
for topic_name, details in [('Topic A', 'Details about Topic A'), ('Topic B', 'Details about Topic B')]:
    rdf_li_topic = ET.SubElement(rdf_Bag_topics, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
    topic_structure = ET.SubElement(rdf_li_topic, "{http://example.com/ns/structured/}TopicStructure")
    topic_name_el = ET.SubElement(topic_structure, "{http://example.com/ns/structured/}Name")
    topic_name_el.text = topic_name
    topic_details_el = ET.SubElement(topic_structure, "{http://example.com/ns/structured/}Details")
    topic_details_el.text = details

# Complex Creator Contact Information with additional details
xmpCreators = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}Creators")
rdf_Seq_creators = ET.SubElement(xmpCreators, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
for creator_name, role in [('John Doe', 'Photographer'), ('Jane Smith', 'Editor')]:
    rdf_li_creator = ET.SubElement(rdf_Seq_creators, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
    creator_structure = ET.SubElement(rdf_li_creator, "{http://example.com/ns/structured/}CreatorStructure")
    creator_name_el = ET.SubElement(creator_structure, "{http://example.com/ns/structured/}Name")
    creator_name_el.text = creator_name
    creator_role_el = ET.SubElement(creator_structure, "{http://example.com/ns/structured/}Role")
    creator_role_el.text = role

# Adding a complex custom data structure
ex_MoreComplexData = ET.SubElement(description, "{http://example.com/ns/}MoreComplexData")
ex_MoreComplexData.text = "This represents a more complex structure with multiple layers and types of data."

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/more_complex_accessibility_features.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"More complex XMP file with advanced structures created at: {xmp_file_path}")
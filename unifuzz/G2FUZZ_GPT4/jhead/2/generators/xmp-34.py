import os
from lxml import etree as ET
from uuid import uuid4

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces including additional ones for Rights, Media Management, custom namespace, and others
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
    'Iptc4xmpExt': "http://iptc.org/std/Iptc4xmpExt/2008-02-29/",
    'plus': "http://ns.useplus.org/ldf/xmp/1.0/",
    'dcTerms': "http://purl.org/dc/terms/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Description for digital asset 1
description1 = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description1.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "Asset 1")
# Add multilingual title
titles = ET.SubElement(description1, "{http://purl.org/dc/elements/1.1/}title")
alt_titles = ET.SubElement(titles, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt")
ET.SubElement(alt_titles, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li", {"{http://www.w3.org/XML/1998/namespace}lang": "en"}).text = "Title in English"
ET.SubElement(alt_titles, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"}).text = "Titre en français"

# Description for digital asset 2 with advanced rights management
description2 = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description2.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "Asset 2")
# Advanced Rights Management with multiple licensees
licensees = ET.SubElement(description2, "{http://ns.useplus.org/ldf/xmp/1.0/}Licensee")
rdf_Bag_licensees = ET.SubElement(licensees, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag")
for licensee_info in ["http://example.org/licensee1", "http://example.org/licensee2"]:
    ET.SubElement(rdf_Bag_licensees, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li").text = licensee_info

# Description for custom structured data
description3 = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description3.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "Custom Data")
# Custom structured data with relationships
related_assets = ET.SubElement(description3, "{http://example.com/ns/}relatedAssets")
rdf_Seq_related_assets = ET.SubElement(related_assets, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
for asset_id in ["Asset123", "Asset456"]:
    ET.SubElement(rdf_Seq_related_assets, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li").text = asset_id

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/advanced_complex_features_v2.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"More complex XMP file created at: {xmp_file_path}")
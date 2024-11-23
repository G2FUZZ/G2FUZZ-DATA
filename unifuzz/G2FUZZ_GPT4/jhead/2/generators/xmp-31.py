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
    'plus': "http://ns.useplus.org/ldf/xmp/1.0/"
}

# Create an RDF (Resource Description Framework) root element
rdf = ET.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=namespaces)

# Create a Description element with accessibility features and more
description = ET.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=namespaces)
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Document history
history = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/mm/}History")
rdf_Seq_history = ET.SubElement(history, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Seq")
# Adding a simple history event as an example
history_event = ET.SubElement(rdf_Seq_history, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li", {
    "{http://ns.adobe.com/xap/1.0/mm/}action": "created",
    "{http://ns.adobe.com/xap/1.0/mm/}instanceID": str(uuid4()),
    "{http://ns.adobe.com/xap/1.0/mm/}when": "2023-01-01T12:00:00Z",
    "{http://ns.adobe.com/xap/1.0/mm/}softwareAgent": "ExampleSoftware/1.0"
})

# Geolocation data
location = ET.SubElement(description, "{http://iptc.org/std/Iptc4xmpExt/2008-02-29/}Location")
location.text = "Eiffel Tower, Paris, France"
gps_latitude = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/g/img/}GPSLatitude")
gps_latitude.text = "48.8584N"
gps_longitude = ET.SubElement(description, "{http://ns.adobe.com/xap/1.0/g/img/}GPSLongitude")
gps_longitude.text = "2.2945E"

# Advanced Rights Management
license_ref = ET.SubElement(description, "{http://ns.useplus.org/ldf/xmp/1.0/}Licensee")
rdf_Bag_license = ET.SubElement(license_ref, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Bag")
rdf_li_license = ET.SubElement(rdf_Bag_license, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
rdf_li_license.text = "http://creativecommons.org/licenses/by/4.0/"

# Custom Structured Data with nested elements
custom_Structure = ET.SubElement(description, "{http://example.com/ns/}CustomStructure")
custom_Field1 = ET.SubElement(custom_Structure, "{http://example.com/ns/}Field1")
custom_Field1.text = "Value1"
nested_Structure = ET.SubElement(custom_Structure, "{http://example.com/ns/}NestedStructure")
nested_Field1 = ET.SubElement(nested_Structure, "{http://example.com/ns/}NestedField1")
nested_Field1.text = "NestedValue1"

# Convert the tree to bytes
xmp_data = ET.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Write the XMP data to a file
xmp_file_path = './tmp/advanced_complex_features.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"Advanced complex XMP file created at: {xmp_file_path}")
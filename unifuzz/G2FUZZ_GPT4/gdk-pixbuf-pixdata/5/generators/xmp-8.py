from lxml import etree

# Define namespaces
ns_map = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
}

# Create root element
rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=ns_map)

# Create Description element
description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")
description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")

# Add title with alternatives
title = etree.SubElement(description, "{http://purl.org/dc/elements/1.1/}title")
alt = etree.SubElement(title, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt")

# English title
li_en = etree.SubElement(alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
li_en.set("{http://www.w3.org/XML/1998/namespace}lang", "en")
li_en.text = "Example Title in English"

# French title
li_fr = etree.SubElement(alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
li_fr.set("{http://www.w3.org/XML/1998/namespace}lang", "fr")
li_fr.text = "Exemple de titre en français"

# Serialize to string
xmp_data = etree.tostring(rdf, pretty_print=True, encoding='UTF-8', xml_declaration=True)

# Save to a file
output_path = './tmp/example.xmp'
with open(output_path, 'wb') as xmp_file:
    xmp_file.write(xmp_data)

print(f"XMP file saved to {output_path}")
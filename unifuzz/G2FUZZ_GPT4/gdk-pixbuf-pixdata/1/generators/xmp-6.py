from lxml import etree

# Define namespaces for XMP
ns_map = {
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'x': "adobe:ns:meta/",
    'xmp': "http://ns.adobe.com/xap/1.0/",
}

# Create RDF root
rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=ns_map)

# Create a Description element with Dublin Core namespace
description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=ns_map)

# Add a title with multiple languages
title = etree.SubElement(description, "{http://purl.org/dc/elements/1.1/}title")
alt = etree.SubElement(title, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Alt")

# English title
li_en = etree.SubElement(alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
li_en.set("{http://www.w3.org/XML/1998/namespace}lang", "en")
li_en.text = "Example XMP File with Internationalization Support"

# French title
li_fr = etree.SubElement(alt, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")
li_fr.set("{http://www.w3.org/XML/1998/namespace}lang", "fr")
li_fr.text = "Exemple de fichier XMP avec support de l'internationalisation"

# Construct the XMP packet
xmpmeta = etree.Element("{adobe:ns:meta/}xmpmeta", nsmap={'x': "adobe:ns:meta/"})
xmpmeta.append(rdf)

# Pretty print
xmp_str = etree.tostring(xmpmeta, pretty_print=True, encoding="UTF-8", xml_declaration=True)

# Save to file
output_path = './tmp/example.xmp'
with open(output_path, 'wb') as f:
    f.write(xmp_str)

print(f"XMP file with internationalization support has been saved to {output_path}")
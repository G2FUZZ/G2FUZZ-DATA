import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata with more complex structures
metadata = {
    'dc:title': {
        'rdf:Alt': {
            'rdf:li': {
                '@xml:lang': 'en',
                '#text': 'Example Title'
            }
        }
    },
    'dc:creator': {
        'rdf:Seq': {
            'rdf:li': 'John Doe'
        }
    },
    'dc:description': {
        'rdf:Alt': {
            'rdf:li': {
                '@xml:lang': 'en',
                '#text': 'An example of an XMP file with complex structures.'
            }
        }
    },
    'xmpRights:UsageTerms': {
        'rdf:Alt': {
            'rdf:li': {
                '@xml:lang': 'en',
                '#text': 'This work is licensed under a Creative Commons Attribution 4.0 International License.'
            }
        }
    }
}

# Create the root element with RDF namespace
rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap={
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/"
})

# Create a Description element for the metadata with necessary namespaces
description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap={
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'dc': "http://purl.org/dc/elements/1.1/",
    'xmpRights': "http://ns.adobe.com/xap/1.0/rights/"
})

# Function to add complex structures
def add_metadata_element(parent, key, value):
    # Split the key to extract the namespace and tag name
    ns, tag = key.split(':', 1) if ':' in key else ('', key)
    # Use the parent's nsmap to get the URI for the namespace, if a namespace is specified
    ns_uri = parent.nsmap[ns] if ns in parent.nsmap else None
    # Create the namespaced tag if a namespace URI was found, otherwise use the tag as is
    namespaced_tag = f"{{{ns_uri}}}{tag}" if ns_uri else tag
    
    if isinstance(value, dict):
        if 'rdf:Alt' in value or 'rdf:Seq' in value or 'rdf:li' in value:
            element = etree.SubElement(parent, namespaced_tag)
            for inner_key, inner_value in value.items():
                add_metadata_element(element, inner_key, inner_value)
        elif '#text' in value and '@xml:lang' in value:
            attrib = {f"{{http://www.w3.org/XML/1998/namespace}}lang": value['@xml:lang']}
            element = etree.SubElement(parent, namespaced_tag, attrib=attrib)
            element.text = value['#text']
        else:
            for inner_key, inner_value in value.items():
                add_metadata_element(parent, inner_key, inner_value)
    else:
        element = etree.SubElement(parent, namespaced_tag)
        element.text = str(value)

# Add metadata fields to the Description
for key, value in metadata.items():
    add_metadata_element(description, key, value)

# Convert the XML structure to a string
xml_bytes = etree.tostring(rdf, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Save the XML to an XMP file
xmp_file_path = './tmp/complex_example_metadata.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(xml_bytes)

print(f"XMP file saved to {xmp_file_path}")
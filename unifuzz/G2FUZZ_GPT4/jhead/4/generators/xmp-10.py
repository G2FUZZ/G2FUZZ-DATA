import os
from lxml import etree

# Define the namespace map to use in the XMP file
NS_MAP = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'xmp': 'http://ns.adobe.com/xap/1.0/',
    'xmpMM': 'http://ns.adobe.com/xap/1.0/mm/',
    'pdf': 'http://ns.adobe.com/pdf/1.3/',
    'photoshop': 'http://ns.adobe.com/photoshop/1.0/',
    'access': 'http://ns.adobe.com/accessibility/1.0/',
}

# Create the root element
rdf = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF', nsmap=NS_MAP)

# Create a Description element for accessibility enhancements
description = etree.SubElement(rdf, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description')
description.set('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about', '')

# Add alternative text descriptions for images as an example of accessibility enhancements
altText = etree.SubElement(description, '{http://ns.adobe.com/accessibility/1.0/}alt')
altText.text = 'An example image showing accessibility enhancements.'

# Create directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Write the XMP to a file
xmp_file_path = os.path.join(output_dir, 'accessibility_enhancements.xmp')
with open(xmp_file_path, 'wb') as f:
    f.write(b'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
    f.write(etree.tostring(rdf, pretty_print=True))
    f.write(b'\n<?xpacket end="w"?>')

print(f'XMP file with accessibility enhancements metadata generated at: {xmp_file_path}')
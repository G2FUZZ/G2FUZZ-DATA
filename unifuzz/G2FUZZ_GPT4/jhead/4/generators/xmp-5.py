import os
from lxml import etree

# Define the XMP data to be written
xmp_data = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/">
        <xmp:Interoperability>
            Through its standardization and RDF base, XMP supports interoperability among different software applications and systems. This means metadata created in one application can be read and understood by another, facilitating easier exchange and processing of digital files.
        </xmp:Interoperability>
    </rdf:Description>
</rdf:RDF>
"""

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the file path
file_path = './tmp/features.xmp'

# Parse the XMP data
xml_root = etree.fromstring(xmp_data)

# Write the XMP file
with open(file_path, 'wb') as file:
    file.write(etree.tostring(xml_root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

print(f"XMP file saved to {file_path}")
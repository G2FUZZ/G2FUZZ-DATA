import os
from lxml import etree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP data to include
xmp_data = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
  <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/">
    <xmp:Extensibility>
        XMP is based on XML, making it flexible and capable of supporting existing and future metadata standards. 
        Users can define their own properties and structures, extending the metadata to meet their specific needs.
    </xmp:Extensibility>
  </rdf:Description>
</rdf:RDF>
"""

# Parse the XMP data
root = ET.fromstring(xmp_data)

# Write the XMP file
xmp_file_path = './tmp/feature_description.xmp'
tree = ET.ElementTree(root)
tree.write(xmp_file_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

print(f'XMP file saved at: {xmp_file_path}')
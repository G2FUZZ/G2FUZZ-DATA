from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template
xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Standardization Across File Formats: XMP provides a standard framework for embedding metadata into digital files, including images, videos, PDFs, and more. This ensures that metadata is consistent and interoperable across different software and platforms.</rdf:li>
    </rdf:Alt>
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Parse the template
root = etree.fromstring(xmp_template)

# Write the XMP file
file_path = './tmp/feature_description.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file created at: {file_path}")
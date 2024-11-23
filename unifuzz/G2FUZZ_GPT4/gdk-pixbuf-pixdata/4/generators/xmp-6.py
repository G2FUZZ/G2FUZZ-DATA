import os
from lxml import etree

# Define the XMP template with the specified feature
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>Integration with Adobe Creative Suite: XMP is deeply integrated with Adobe's suite of creative software, including Photoshop, Illustrator, and InDesign. This allows users to easily view, edit, and manage metadata within these applications.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(output_dir, 'feature.xmp')

# Write the XMP content to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(etree.tostring(etree.fromstring(xmp_content), pretty_print=True, encoding='unicode'))

print(f"XMP file has been successfully created at: {file_path}")
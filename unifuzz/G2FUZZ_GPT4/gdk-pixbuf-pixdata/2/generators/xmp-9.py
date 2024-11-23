from lxml import etree
import os

# Create tmp directory if it doesn't exist
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the XMP structure
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:description>
      <rdf:Alt>
        <rdf:li xml:lang="en">By embedding descriptive and relevant metadata within files, XMP enhances the searchability of digital assets. This makes it easier to find, organize, and manage files based on their content and characteristics.</rdf:li>
      </rdf:Alt>
    </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Parse the XMP content
xmp_tree = etree.fromstring(xmp_content)

# Define the file name
file_name = "feature_searchability.xmp"

# Save the XMP file
with open(os.path.join(output_dir, file_name), "wb") as f:
    f.write(etree.tostring(xmp_tree, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

print(f"XMP file '{file_name}' has been saved to '{output_dir}'.")
import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template
xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>Searchability: By providing standardized, structured metadata, XMP enhances the searchability of files. Metadata can be indexed by search engines or internal search tools, making it easier to locate files based on their content, creation details, or usage rights.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

def save_xmp_file(file_path, content):
    # Parse the XML content
    root = etree.fromstring(content)
    # Pretty print and encode to bytes
    pretty_xml = etree.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True)
    
    # Write the pretty printed XML to the file
    with open(file_path, 'wb') as file:
        file.write(pretty_xml)

# Define the path for the new XMP file
xmp_file_path = './tmp/searchability_metadata.xmp'

# Save the XMP content to the file
save_xmp_file(xmp_file_path, xmp_template)
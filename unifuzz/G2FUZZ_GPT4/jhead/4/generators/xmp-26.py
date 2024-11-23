import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with more complex structures
xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c015 81.157285, 2020/06/15-02:41:56        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
          xmlns:dc="http://purl.org/dc/elements/1.1/"
          xmlns:xmp="http://ns.adobe.com/xap/1.0/"
          xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
          xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
  <rdf:Description rdf:about=""
    dc:description="Complex File Structure Example"
    dc:creator="John Doe"
    dc:title="Complex XMP Example"
    photoshop:City="New York"
    photoshop:Country="USA"
    xmp:CreatorTool="My Custom Tool"
    xmpRights:UsageTerms="Copyrighted Work. All rights reserved."
    xmpRights:Marked="True">
    <dc:subject>
      <rdf:Bag>
        <rdf:li>XMP</rdf:li>
        <rdf:li>Metadata</rdf:li>
        <rdf:li>Complex Structure</rdf:li>
      </rdf:Bag>
    </dc:subject>
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
xmp_file_path = './tmp/complex_metadata.xmp'

# Save the XMP content to the file
save_xmp_file(xmp_file_path, xmp_template)
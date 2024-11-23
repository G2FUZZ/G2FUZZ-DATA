from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with a more complex structure
xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014 79.159824, 2016/09/10-02:41:30        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Standardization Across File Formats</rdf:li>
    </rdf:Alt>
   </dc:description>
  </rdf:Description>
  <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <xmp:CreatorTool>Custom Tool</xmp:CreatorTool>
   <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
  </rdf:Description>
  <rdf:Description rdf:about="" xmlns:customns="http://example.com/ns/">
   <customns:Property>Custom Value</customns:Property>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Parse the template
root = etree.fromstring(xmp_template)

# Add additional metadata or modify the template as needed here

# Write the XMP file
file_path = './tmp/complex_feature_description.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file created at: {file_path}")
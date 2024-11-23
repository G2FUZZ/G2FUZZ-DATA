import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with RDF content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:ex="http://example.com/xmp/1.0/">
   <ex:Feature>RDF-Based: XMP is based on the Resource Description Framework (RDF), a standard model for data interchange on the web. This makes XMP metadata highly structured and enables sophisticated metadata schemes, including hierarchical and relational data.</ex:Feature>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Parse the XMP content to ensure its correctness
root = etree.fromstring(xmp_content)

# Define the file path
file_path = './tmp/feature_xmp_file.xmp'

# Write the content to an XMP file
with open(file_path, 'wb') as file:
    file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'XMP file saved at {file_path}')
import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with a custom namespace and field
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.0-c060 61.134777, 2010/02/12-17:32:00        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:custom="http://example.com/customns#">
   <custom:Feature>Extensibility</custom:Feature>
   <custom:Description>Allows custom metadata fields in addition to the standard ones, enabling users to add specific information relevant to their needs or industry standards without altering the original content.</custom:Description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Parse the XMP template to ensure its correctness
root = etree.fromstring(xmp_template)

# Write the XMP data to a file
xmp_file_path = './tmp/custom_metadata.xmp'
with open(xmp_file_path, 'wb') as file:
    file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file with custom metadata has been saved to {xmp_file_path}")
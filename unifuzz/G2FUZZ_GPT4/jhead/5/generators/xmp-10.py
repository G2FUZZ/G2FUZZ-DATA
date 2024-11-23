from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# XMP base structure
xmp_base = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:description>
        <rdf:Alt>
          <rdf:li xml:lang="x-default">Compatibility and Interoperability: Despite its origins within Adobe, XMP is an open standard, ensuring its compatibility and interoperability with a wide range of software applications and digital asset management systems.</rdf:li>
        </rdf:Alt>
      </dc:description>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Parse the XMP structure to ensure correctness
xml_root = etree.fromstring(xmp_base)

# Write to file
file_path = './tmp/feature_description.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(xml_root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'XMP file saved to {file_path}')
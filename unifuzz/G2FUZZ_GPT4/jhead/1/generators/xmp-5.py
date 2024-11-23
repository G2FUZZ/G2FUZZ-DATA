import os
from datetime import datetime
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with rich metadata support
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  
  <!-- Dublin Core Metadata -->
  <rdf:Description rdf:about=""
   xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:format>application/pdf</dc:format>
   <dc:title>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Sample PDF</rdf:li>
    </rdf:Alt>
   </dc:title>
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">This is a sample PDF file with rich metadata support.</rdf:li>
    </rdf:Alt>
   </dc:description>
   <dc:creator>
    <rdf:Seq>
     <rdf:li>John Doe</rdf:li>
    </rdf:Seq>
   </dc:creator>
   <dc:subject>
    <rdf:Bag>
     <rdf:li>Metadata</rdf:li>
     <rdf:li>XMP</rdf:li>
     <rdf:li>Sample</rdf:li>
    </rdf:Bag>
   </dc:subject>
  </rdf:Description>
  
  <!-- IPTC Metadata -->
  <rdf:Description rdf:about=""
   xmlns:Iptc4xmpCore="http://iptc.org/std/Iptc4xmpCore/1.0/xmlns/">
   <Iptc4xmpCore:LocationCode>XMP</Iptc4xmpCore:LocationCode>
   <Iptc4xmpCore:City>Sample City</Iptc4xmpCore:City>
   <Iptc4xmpCore:CountryCode>XX</Iptc4xmpCore:CountryCode>
   <Iptc4xmpCore:CountryName>Sample Country</Iptc4xmpCore:CountryName>
  </rdf:Description>
  
  <!-- EXIF Metadata -->
  <rdf:Description rdf:about=""
   xmlns:exif="http://ns.adobe.com/exif/1.0/">
   <exif:Make>Sample Make</exif:Make>
   <exif:Model>Sample Model</exif:Model>
   <exif:DateTimeOriginal>2023-01-01T12:00:00</exif:DateTimeOriginal>
  </rdf:Description>
  
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Parse the XMP string to ensure its validity
root = etree.fromstring(xmp_template.encode('utf-8'))

# Convert the XML back to a pretty-printed string
xml_bytes = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Define the file path
file_path = './tmp/sample_metadata.xmp'

# Write the XMP content to a file
with open(file_path, 'wb') as file:
    file.write(xml_bytes)

print(f'Successfully created XMP file at {file_path}')
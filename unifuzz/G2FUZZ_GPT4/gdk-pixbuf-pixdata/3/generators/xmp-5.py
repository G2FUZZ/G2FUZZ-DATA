import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:exif="http://ns.adobe.com/exif/1.0/">
    <dc:format>image/jpeg</dc:format>
    <photoshop:Credit>Photographer Name</photoshop:Credit>
    <photoshop:CopyrightNotice>&#xA9; 2021 Photographer Name</photoshop:CopyrightNotice>
    <xmp:CreateDate>2021-07-01T12:00:00</xmp:CreateDate>
    <exif:DateTimeOriginal>2021-07-01T12:00:00</exif:DateTimeOriginal>
    <exif:UserComment>This is an example of EXIF user comment.</exif:UserComment>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Parse the XML to ensure correctness
root = etree.fromstring(xmp_template)

# Save the XMP data to a file
file_path = './tmp/example.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file saved to {file_path}")
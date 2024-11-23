from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Extended XMP structure with custom namespaces and additional metadata fields
xmp_base = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
           xmlns:dc="http://purl.org/dc/elements/1.1/"
           xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
           xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
    <rdf:Description rdf:about=""
      dc:format="image/jpeg"
      photoshop:ColorMode="3"
      photoshop:ICCProfile="Adobe RGB (1998)">
      <dc:title>
        <rdf:Alt>
          <rdf:li xml:lang="en">Sample Image</rdf:li>
          <rdf:li xml:lang="fr">Image d'exemple</rdf:li>
        </rdf:Alt>
      </dc:title>
      <dc:creator>
        <rdf:Seq>
          <rdf:li>John Doe</rdf:li>
          <rdf:li>Jane Doe</rdf:li>
        </rdf:Seq>
      </dc:creator>
      <dc:description>
        <rdf:Alt>
          <rdf:li xml:lang="en">A brief description of the image.</rdf:li>
          <rdf:li xml:lang="de">Eine kurze Beschreibung des Bildes.</rdf:li>
        </rdf:Alt>
      </dc:description>
      <dc:rights>
        <rdf:Alt>
          <rdf:li xml:lang="en">© 2023 John Doe. All rights reserved.</rdf:li>
        </rdf:Alt>
      </dc:rights>
      <dc:subject>
        <rdf:Bag>
          <rdf:li>photography</rdf:li>
          <rdf:li>sample</rdf:li>
          <rdf:li>metadata</rdf:li>
        </rdf:Bag>
      </dc:subject>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Parse the XMP structure to ensure correctness
xml_root = etree.fromstring(xmp_base)

# Write to file
file_path = './tmp/extended_feature_description.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(xml_root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'Extended XMP file saved to {file_path}')
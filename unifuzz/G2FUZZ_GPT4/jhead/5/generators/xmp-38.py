from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Extended XMP structure with more complex features and custom namespaces
xmp_base = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
           xmlns:dc="http://purl.org/dc/elements/1.1/"
           xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
           xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
           xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
           xmlns:exif="http://ns.adobe.com/exif/1.0/">
    <rdf:Description rdf:about=""
      dc:format="image/jpeg"
      photoshop:ColorMode="3"
      photoshop:ICCProfile="Adobe RGB (1998)"
      xmpRights:UsageTerms="This is a custom usage term"
      exif:Make="Nikon"
      exif:Model="D850">
      <dc:title>
        <rdf:Alt>
          <rdf:li xml:lang="en">Advanced Sample Image</rdf:li>
          <rdf:li xml:lang="fr">Image d'exemple avancée</rdf:li>
        </rdf:Alt>
      </dc:title>
      <dc:creator>
        <rdf:Seq>
          <rdf:li>John Doe</rdf:li>
          <rdf:li>Jane Doe</rdf:li>
          <rdf:li>Extra Author</rdf:li>
        </rdf:Seq>
      </dc:creator>
      <dc:description>
        <rdf:Alt>
          <rdf:li xml:lang="en">An extended description of the image with more details.</rdf:li>
          <rdf:li xml:lang="de">Eine erweiterte Beschreibung des Bildes mit mehr Details.</rdf:li>
        </rdf:Alt>
      </dc:description>
      <dc:rights>
        <rdf:Alt>
          <rdf:li xml:lang="en">© 2023 John Doe. All rights reserved. Extended License.</rdf:li>
        </rdf:Alt>
      </dc:rights>
      <dc:subject>
        <rdf:Bag>
          <rdf:li>advanced photography</rdf:li>
          <rdf:li>extended sample</rdf:li>
          <rdf:li>complex metadata</rdf:li>
          <rdf:li>additional subject</rdf:li>
        </rdf:Bag>
      </dc:subject>
      <!-- Custom Properties -->
      <Iptc4xmpExt:Event>Sample Event</Iptc4xmpExt:Event>
      <Iptc4xmpExt:LocationCreated>
        <rdf:Bag>
          <rdf:li>New York</rdf:li>
          <rdf:li>Paris</rdf:li>
        </rdf:Bag>
      </Iptc4xmpExt:LocationCreated>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Parse the XMP structure to ensure correctness
xml_root = etree.fromstring(xmp_base)

# Write to file
file_path = './tmp/advanced_extended_feature_description.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(xml_root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'Advanced extended XMP file saved to {file_path}')
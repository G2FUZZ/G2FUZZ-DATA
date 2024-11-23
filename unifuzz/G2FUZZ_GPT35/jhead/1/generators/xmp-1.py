import os
from datetime import datetime
from lxml import etree

# Create the XMP file content
xmp_template = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2019/03/13-16:12:05        ">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about="" xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
      <xmpRights:Marked>True</xmpRights:Marked>
    </rdf:Description>
    <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:creator>
        <rdf:Seq>
          <rdf:li>Your Name</rdf:li>
        </rdf:Seq>
      </dc:creator>
      <dc:description>
        <rdf:Alt>
          <rdf:li xml:lang="x-default">Description of the file</rdf:li>
        </rdf:Alt>
      </dc:description>
      <dc:rights>
        <rdf:Alt>
          <rdf:li xml:lang="x-default">Copyright information</rdf:li>
        </rdf:Alt>
      </dc:rights>
      <dc:subject>
        <rdf:Bag>
          <rdf:li>Keyword1</rdf:li>
          <rdf:li>Keyword2</rdf:li>
        </rdf:Bag>
      </dc:subject>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create tmp directory if it doesn't exist
os.makedirs("tmp", exist_ok=True)

# Save the XMP file
file_name = f"./tmp/metadata_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xmp"
with open(file_name, "w") as xmp_file:
    xmp_file.write(xmp_template)

print(f"XMP file saved as: {file_name}")
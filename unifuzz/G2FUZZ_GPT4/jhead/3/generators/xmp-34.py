import os
import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP content with a more complex structure
xmp_content = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
          xmlns:dc="http://purl.org/dc/elements/1.1/"
          xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
          xmlns:xmp="http://ns.adobe.com/xap/1.0/"
          xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">

  <!-- First Description Block -->
  <rdf:Description rdf:about=""
        dc:format="image/jpeg"
        dc:title="Sunset"
        dc:description="A beautiful sunset at the beach."
        photoshop:Credit="John Doe Photography"
        photoshop:City="Los Angeles"
        photoshop:Country="United States"
        xmp:CreateDate="{datetime.datetime.now().isoformat()}"
        xmp:CreatorTool="Adobe Photoshop"
        xmpRights:Marked="True">
    <dc:creator>
      <rdf:Seq>
        <rdf:li>John Doe</rdf:li>
      </rdf:Seq>
    </dc:creator>
    <dc:subject>
      <rdf:Bag>
        <rdf:li>Sunset</rdf:li>
        <rdf:li>Beach</rdf:li>
        <rdf:li>Photography</rdf:li>
      </rdf:Bag>
    </dc:subject>
  </rdf:Description>

  <!-- Second Description Block with Nested Structures -->
  <rdf:Description rdf:about=""
        xmlns:aux="http://ns.adobe.com/exif/1.0/aux/"
        aux:Lens="EF24-105mm f/4L IS USM"
        aux:LensInfo="24/1 105/1 0/0 0/0">
    <aux:LensSerialNumber>0000000000</aux:LensSerialNumber>
  </rdf:Description>

 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Path to the XMP file to be created
xmp_file_path = './tmp/complex_structure_description.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f"XMP file created at {xmp_file_path}")
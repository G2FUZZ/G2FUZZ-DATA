import os
from lxml import etree

# Create a directory if it does not exist
os.makedirs("./tmp/", exist_ok=True)

# Generate XMP file with Thumbnail Preview
xmp_file_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c067 79.157747, 2015/03/30-23:40:42        ">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
      <xmp:Thumbnails>
        <rdf:Alt>
          <rdf:li rdf:parseType="Resource">
            <xmp:format>JPEG</xmp:format>
            <xmp:image>ThumbnailImageDataAsBase64EncodedString</xmp:image>
          </rdf:li>
        </rdf:Alt>
      </xmp:Thumbnails>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Save the generated XMP file
file_path = "./tmp/thumbnail_preview.xmp"
with open(file_path, "w") as xmp_file:
    xmp_file.write(xmp_file_content)

print(f"XMP file with Thumbnail Preview generated at: {file_path}")
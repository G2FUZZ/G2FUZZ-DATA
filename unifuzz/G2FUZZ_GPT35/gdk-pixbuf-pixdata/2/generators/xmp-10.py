import os

# Define the content to be written in the xmp file
xmp_content = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c067 79.157747, 2015/03/30-23:40:42 ">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:xmp="adobe:ns:meta/"
        xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
        xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#">
      <dc:description><rdf:Alt><rdf:li xml:lang="x-default">XMP incorporates elements from the Dublin Core Metadata Initiative for enhanced interoperability and metadata consistency.</rdf:li></rdf:Alt></dc:description>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
"""
# Create the directory if it doesn't exist
if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

# Write the content to the xmp file
with open("./tmp/dublin_core.xmp", "w") as file:
    file.write(xmp_content)

print("XMP file with Dublin Core Integration features has been generated and saved in ./tmp/ directory.")
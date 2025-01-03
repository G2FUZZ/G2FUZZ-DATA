import os
from lxml import etree

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a sample XMP file
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
 <x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
     <rdf:Description rdf:about=""
           xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
       <xmpRights:Marked>True</xmpRights:Marked>
     </rdf:Description>
   </rdf:RDF>
 </x:xmpmeta>
<?xpacket end="w"?>
"""

# Save the XMP file
with open('./tmp/sample.xmp', 'w') as file:
    file.write(xmp_content)
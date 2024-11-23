import os

xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <xmp:Rating>5</xmp:Rating>
         <xmp:CreateDate>2022-01-01</xmp:CreateDate>
         <xmp:Embeddable>true</xmp:Embeddable>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

with open('./tmp/sample_file.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated successfully.")
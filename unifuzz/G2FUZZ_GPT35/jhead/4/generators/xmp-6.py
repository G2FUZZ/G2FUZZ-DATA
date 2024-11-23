import os

xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Preservation>XMP metadata can be preserved across different software applications and platforms.</xmp:Preservation>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

with open('./tmp/preservation.xmp', 'w') as file:
    file.write(xmp_content)
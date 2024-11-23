import os

xmp_content = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
            <xmpRights:Marked>True</xmpRights:Marked>
            <xmpRights:WebStatement>https://www.example.com/rights</xmpRights:WebStatement>
            <xmpRights:UsageTerms>Usage terms here</xmpRights:UsageTerms>
            <xmpRights:UsageRights>Usage rights here</xmpRights:UsageRights>
            <xmpRights:Certificate>License certificate here</xmpRights:Certificate>
            <xmpRights:Owner>Owner's name here</xmpRights:Owner>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

filename = './tmp/rights_management.xmp'

with open(filename, 'w') as file:
    file.write(xmp_content)

print(f'XMP file with rights management features saved at: {filename}')
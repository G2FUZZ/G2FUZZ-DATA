import os
from lxml import etree

# Create the XMP file content
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c142 79.160924, 2017/07/13-01:06:39        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
            <xmpRights:Marked>True</xmpRights:Marked>
            <xmpRights:WebStatement>https://www.example.com/rights</xmpRights:WebStatement>
            <xmpRights:UsageTerms>Copyrighted</xmpRights:UsageTerms>
            <xmpRights:Owner>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                </rdf:Seq>
            </xmpRights:Owner>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create the directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the XMP file
file_path = os.path.join(directory, 'rights_management.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
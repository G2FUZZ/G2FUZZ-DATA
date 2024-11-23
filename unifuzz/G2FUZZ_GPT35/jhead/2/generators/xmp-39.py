import os

# Create the XMP file content with multiple owners
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
                    <rdf:li>
                        <rdf:Description>
                            <xmpRights:OwnerName>John Doe</xmpRights:OwnerName>
                            <xmpRights:OwnerEmail>john.doe@example.com</xmpRights:OwnerEmail>
                        </rdf:Description>
                    </rdf:li>
                    <rdf:li>
                        <rdf:Description>
                            <xmpRights:OwnerName>Jane Smith</xmpRights:OwnerName>
                            <xmpRights:OwnerEmail>jane.smith@example.com</xmpRights:OwnerEmail>
                        </rdf:Description>
                    </rdf:li>
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

# Save the XMP file with multiple owners
file_path = os.path.join(directory, 'rights_management_extended.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"Extended XMP file saved at: {file_path}")
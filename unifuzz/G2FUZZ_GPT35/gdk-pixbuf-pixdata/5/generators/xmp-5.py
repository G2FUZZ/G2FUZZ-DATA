import os

# Create a directory to save the xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with the specified feature
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#">
            <xmp:CreatorTool>Python</xmp:CreatorTool>
            <xmp:ModifyDate>2022-09-30T18:43:29</xmp:ModifyDate>
            <xmpMM:DocumentID>uuid:1234567890</xmpMM:DocumentID>
            <xmpMM:InstanceID>uuid:0987654321</xmpMM:InstanceID>
            <xmp:Version>XMP Version 1.1</xmp:Version>
            <xmpMM:Versions>
                <rdf:Seq>
                    <rdf:li>XMP Version 1.0</rdf:li>
                    <rdf:li>XMP Version 1.2</rdf:li>
                    <rdf:li>XMP Version 2.0</rdf:li>
                </rdf:Seq>
            </xmpMM:Versions>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

file_path = './tmp/versioning.xmp'
with open(file_path, 'w') as f:
    f.write(xmp_content)

print(f'XMP file with versioning feature generated and saved at: {file_path}')
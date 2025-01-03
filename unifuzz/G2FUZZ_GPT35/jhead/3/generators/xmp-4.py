import os

# Create a directory to save xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files
metadata = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c067 79.157747, 2015/03/30-23:40:42        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:CreateDate>2022-09-25T10:30:00</xmp:CreateDate>
            <xmp:CreatorTool>Python</xmp:CreatorTool>
            <xmp:MetadataDate>2022-09-25T10:30:00</xmp:MetadataDate>
            <xmp:ModifyDate>2022-09-25T10:30:00</xmp:ModifyDate>
            <xmp:Nickname>Generated</xmp:Nickname>
            <xmp:Standardized>True</xmp:Standardized>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

file_names = ['file1.xmp', 'file2.xmp', 'file3.xmp']

for file_name in file_names:
    with open(f'./tmp/{file_name}', 'w') as f:
        f.write(metadata)
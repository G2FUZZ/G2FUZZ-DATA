import os

metadata = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:ModifyDate>2022-02-15T10:00:00</xmp:ModifyDate>
            <xmp:Version>1.0</xmp:Version>
            <xmp:CustomField1>Custom Value 1</xmp:CustomField1>
            <xmp:CustomField2>Custom Value 2</xmp:CustomField2>
        </rdf:Description>
        <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:creator>John Doe</dc:creator>
            <dc:title>Sample Title</dc:title>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

filename = './tmp/metadata_extended.xmp'

with open(filename, 'w') as f:
    f.write(metadata)

print(f'Extended XMP file with custom metadata entries saved at: {filename}')
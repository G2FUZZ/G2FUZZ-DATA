import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with complex file structures
xmp_content = """<?xpacket begin='ï»¿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.158924, 2015/09/29-01:07:23">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/" xmlns:dc="http://purl.org/dc/elements/1.1/">
            <xmp:ModifyDate>2022-10-01T12:00:00</xmp:ModifyDate>
            <xmp:MetadataDate>2022-10-01T12:00:00</xmp:MetadataDate>
            <xmp:CreateDate>2022-10-01T12:00:00</xmp:CreateDate>
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:Version>2.0</xmp:Version>
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Sample Title</rdf:li>
                </rdf:Alt>
            </dc:title>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>Author 1</rdf:li>
                    <rdf:li>Author 2</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:description>
                <rdf:Bag>
                    <rdf:li xml:lang="en">Description in English</rdf:li>
                    <rdf:li xml:lang="fr">Description en français</rdf:li>
                </rdf:Bag>
            </dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Save the XMP file with complex file structures
with open('./tmp/complex_xmp.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with complex file structures generated and saved successfully.")
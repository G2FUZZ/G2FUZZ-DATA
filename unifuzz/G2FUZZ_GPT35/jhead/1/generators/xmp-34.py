import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with even more complex file structures
xmp_content = """<?xpacket begin='ï»¿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.158924, 2015/09/29-01:07:23">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:ModifyDate>2022-10-01T12:00:00</xmp:ModifyDate>
            <xmp:MetadataDate>2022-10-01T12:00:00</xmp:MetadataDate>
            <xmp:CreateDate>2022-10-01T12:00:00</xmp:CreateDate>
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:Version>2.0</xmp:Version>
            <xmp:ArrayProp>
                <rdf:Bag>
                    <rdf:li>Item1</rdf:li>
                    <rdf:li>Item2</rdf:li>
                </rdf:Bag>
            </xmp:ArrayProp>
        </rdf:Description>
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:CustomField1>Value1</custom:CustomField1>
            <custom:CustomField2>Value2</custom:CustomField2>
            <custom:CustomArrayProp>
                <rdf:Seq>
                    <rdf:li>Element1</rdf:li>
                    <rdf:li>Element2</rdf:li>
                </rdf:Seq>
            </custom:CustomArrayProp>
        </rdf:Description>
        <rdf:Description rdf:about="" xmlns:exif="http://ns.adobe.com/exif/1.0/">
            <exif:UserComment>This is a user comment</exif:UserComment>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Save the XMP file with even more complex file structures
with open('./tmp/extended_complex_versioning.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with even more complex file structures generated and saved successfully.")
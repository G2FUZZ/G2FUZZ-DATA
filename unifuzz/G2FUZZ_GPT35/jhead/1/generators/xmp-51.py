import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with more complex file structures
xmp_content = """<?xpacket begin='ï»¿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c123 77.159949, 2021/08/02-13:17:09">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:exif="http://ns.adobe.com/exif/1.0/"
             xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
             xmlns:custom="http://example.com/custom/1.0/">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/"
                         xmlns:dc="http://purl.org/dc/elements/1.1/"
                         xmlns:custom="http://example.com/custom/1.0/">
            <xmp:ModifyDate>2022-10-01T12:00:00</xmp:ModifyDate>
            <xmp:MetadataDate>2022-10-01T12:00:00</xmp:MetadataDate>
            <xmp:CreateDate>2022-10-01T12:00:00</xmp:CreateDate>
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:Version>3.0</xmp:Version>
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
            <custom:customField>
                <rdf:Bag>
                    <rdf:li>Custom Value 1</rdf:li>
                    <rdf:li>Custom Value 2</rdf:li>
                </rdf:Bag>
            </custom:customField>
            <exif:Exif>
                <exif:DateTimeOriginal>2022-10-01T12:00:00</exif:DateTimeOriginal>
            </exif:Exif>
            <photoshop:Document>
                <photoshop:ColorMode>RGB</photoshop:ColorMode>
            </photoshop:Document>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Save the XMP file with more complex file structures
with open('./tmp/more_complex_xmp.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with more complex file structures generated and saved successfully.")
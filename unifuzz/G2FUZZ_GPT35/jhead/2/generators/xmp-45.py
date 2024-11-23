import os

# Define the content of the XMP file with even more complex features
xmp_content_extended = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:exif="http://ns.adobe.com/exif/1.0/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
            xmlns:custom="http://example.com/custom/1.0/">
            <xmpMM:DocumentID>uuid:4B8A9F8E-0F9E-4C20-8A7B-373D1B9A7BBF</xmpMM:DocumentID>
            <exif:ExposureTime>1/60</exif:ExposureTime>
            <exif:FNumber>5.6</exif:FNumber>
            <exif:DateTimeOriginal>2021-12-01T12:00:00</exif:DateTimeOriginal>
            <photoshop:Credit>John Doe</photoshop:Credit>
            <photoshop:Headline>Sample Image</photoshop:Headline>
            <custom:Location>
                <custom:City>New York</custom:City>
                <custom:Country>USA</custom:Country>
                <custom:Coordinates>
                    <custom:Latitude>40.7128</custom:Latitude>
                    <custom:Longitude>-74.0060</custom:Longitude>
                </custom:Coordinates>
            </custom:Location>
            <custom:Tags>
                <rdf:Bag>
                    <rdf:li>Tag1</rdf:li>
                    <rdf:li>Tag2</rdf:li>
                    <rdf:li>Tag3</rdf:li>
                </rdf:Bag>
            </custom:Tags>
            <custom:Description>
                <custom:Summary>This is a sample description.</custom:Summary>
                <custom:Details>This image was taken in downtown Manhattan.</custom:Details>
            </custom:Description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the extended XMP file with complex features to ./tmp/
with open('./tmp/extended_metadata_extended.xmp', 'w') as file:
    file.write(xmp_content_extended)

print("Extended XMP file with more complex structures generated and saved successfully.")
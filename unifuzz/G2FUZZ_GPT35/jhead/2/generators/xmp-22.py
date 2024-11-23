import os

# Define the content of the XMP file with more complex features
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:exif="http://ns.adobe.com/exif/1.0/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
            <xmpMM:DocumentID>uuid:4B8A9F8E-0F9E-4C20-8A7B-373D1B9A7BBF</xmpMM:DocumentID>
            <exif:ExposureTime>1/60</exif:ExposureTime>
            <exif:FNumber>5.6</exif:FNumber>
            <exif:DateTimeOriginal>2021-12-01T12:00:00</exif:DateTimeOriginal>
            <photoshop:Credit>John Doe</photoshop:Credit>
            <photoshop:Headline>Sample Image</photoshop:Headline>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the XMP file with complex features to ./tmp/
with open('./tmp/extended_metadata.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file generated and saved successfully.")
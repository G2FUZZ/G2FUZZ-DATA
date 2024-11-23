import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file with complex file structures
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:custom="http://example.com/custom/"
            xmp:CreatorTool="Python"
            xmpMM:DocumentID="uuid:1234567890"
            xmpMM:InstanceID="uuid:0987654321"
            xmpMM:OriginalDocumentID="uuid:abcdef123456"
            xmpMM:RenditionClass="proof:pdf"
            xmpMM:VersionID="1.0">
            <custom:CustomField1>Value1</custom:CustomField1>
            <custom:CustomField2>Value2</custom:CustomField2>
            <rdf:Bag>
                <rdf:li>Item 1</rdf:li>
                <rdf:li>Item 2</rdf:li>
            </rdf:Bag>
            <rdf:Seq>
                <rdf:li>Item 3</rdf:li>
                <rdf:li>Item 4</rdf:li>
            </rdf:Seq>
        </rdf:Description>
        <rdf:Description rdf:about=""
            xmlns:exif="http://ns.adobe.com/exif/1.0/"
            exif:ExifVersion="2.1"
            exif:ColorSpace="sRGB">
            <exif:GPSInfo>
                <rdf:Altitude>123.45</rdf:Altitude>
                <rdf:Latitude>40.7128</rdf:Latitude>
                <rdf:Longitude>-74.0060</rdf:Longitude>
            </exif:GPSInfo>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

file_name = 'extended_complex_file.xmp'
file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file '{file_name}' with more complex file structures generated and saved in '{directory}'")
import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with additional complex file features
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
            xmlns:exif="http://ns.adobe.com/exif/1.0/">
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="en">XMP file with complex features</rdf:li>
                </rdf:Alt>
            </dc:description>
            <photoshop:Headline>Complex XMP File</photoshop:Headline>
            <exif:ExposureTime>1/100</exif:ExposureTime>
            <exif:FNumber>5.6</exif:FNumber>
            <exif:ISOSpeed>200</exif:ISOSpeed>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

with open('./tmp/complex_feature_xmp.xmp', 'w') as file:
    file.write(xmp_content)

print("Complex XMP file generated successfully.")
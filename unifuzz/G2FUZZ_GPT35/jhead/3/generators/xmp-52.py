import os

# Define the XMP content with more complex file structures
xmp_content_complex = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:exif="http://ns.adobe.com/exif/1.0/"
             xmlns:xmp="http://ns.adobe.com/xap/1.0/"
             xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Complex XMP File</rdf:li>
                </rdf:Alt>
            </dc:title>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">This XMP file contains complex metadata structures.</rdf:li>
                </rdf:Alt>
            </dc:description>
            <exif:DateTimeOriginal>2022-01-01T12:00:00</exif:DateTimeOriginal>
            <xmp:CreatorTool>Adobe Photoshop</xmp:CreatorTool>
            <photoshop:Credit>John Doe</photoshop:Credit>
            <xmpRights:UsageTerms>For internal use only</xmpRights:UsageTerms>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the complex XMP file
with open('./tmp/complex.xmp', 'w') as f:
    f.write(xmp_content_complex)

print("Complex XMP file generated successfully in './tmp/' directory.")
import os

# Define the XMP content with even more complex file structures
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:exif="http://ns.adobe.com/exif/1.0/"
             xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
             xmlns:custom="http://example.com/custom/1.0/">
        <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/"
                         xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Even More Complex Extended XMP File</rdf:li>
                </rdf:Alt>
            </dc:title>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">This XMP file contains even more complex extended metadata information.</rdf:li>
                </rdf:Alt>
            </dc:description>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Smith</rdf:li>
                    <rdf:li>Emily Brown</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:subject>
                <rdf:Bag>
                    <rdf:li>Keyword1</rdf:li>
                    <rdf:li>Keyword2</rdf:li>
                    <rdf:li>Keyword3</rdf:li>
                    <rdf:li>Keyword4</rdf:li>
                </rdf:Bag>
            </dc:subject>
            <exif:CameraModel>XYZ123</exif:CameraModel>
            <photoshop:ColorMode>RGB</photoshop:ColorMode>
            <xmp:Rating>5</xmp:Rating>
            <custom:CustomField1>Custom Value 1</custom:CustomField1>
            <custom:CustomField2>Custom Value 2</custom:CustomField2>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the extended XMP file
with open('./tmp/even_more_complex_extended.xmp', 'w') as f:
    f.write(xmp_content)

print("Even More Complex Extended XMP file generated successfully in './tmp/' directory.")
import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file content with multiple RDF descriptions and namespaces
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:CreatorTool>Adobe Photoshop</xmp:CreatorTool>
            <xmp:CreateDate>2022-01-01T12:00:00</xmp:CreateDate>
            <xmp:Rating>5</xmp:Rating>
        </rdf:Description>
        <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:title>Sample Image</dc:title>
            <dc:creator>John Doe</dc:creator>
            <dc:date>2022-01-01</dc:date>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Save the generated XMP file
with open('./tmp/extended_metadata.xmp', 'w') as file:
    file.write(xmp_content)
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with Thumbnail Preview feature
xmp_content = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:xmp='http://ns.adobe.com/xap/1.0/'>
            <xmp:Thumbnails>
                <rdf:Alt>
                    <rdf:li>Thumbnail Preview: XMP files can include thumbnail previews for quick visual identification.</rdf:li>
                </rdf:Alt>
            </xmp:Thumbnails>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the XMP file to ./tmp/ directory
file_path = './tmp/thumbnail_preview.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file with Thumbnail Preview feature saved at: {file_path}")
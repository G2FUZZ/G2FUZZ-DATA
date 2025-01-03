import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file
file_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <xmp:ModifyDate>2022-10-10T12:00:00Z</xmp:ModifyDate>
            <dc:description>File Integrity: XMP metadata can help verify the authenticity and integrity of a file by providing a record of its history and modifications.</dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

with open('./tmp/file_integrity.xmp', 'w') as f:
    f.write(file_content)

print("XMP file generated successfully.")
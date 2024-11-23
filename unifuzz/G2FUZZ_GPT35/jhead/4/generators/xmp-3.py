import os

# Create a directory to store generated xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP files
xmp_data = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='XMP Core 4.4.0'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:format>image/jpeg</dc:format>
            <dc:format>image/tiff</dc:format>
            <dc:format>application/pdf</dc:format>
            <dc:format>image/vnd.adobe.photoshop</dc:format>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

file_path = './tmp/embedded_xmp.xmp'

with open(file_path, 'w') as f:
    f.write(xmp_data)

print(f"XMP file generated at: {file_path}")
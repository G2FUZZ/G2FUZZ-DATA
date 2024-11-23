import os

# Generate xmp file content
xmp_content = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:title>Example Title</dc:title>
            <dc:creator>John Doe</dc:creator>
            <dc:description>Example Description</dc:description>
            <dc:publisher>Publisher Name</dc:publisher>
            <dc:date>2022-10-01</dc:date>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Create directory if not exists
os.makedirs('./tmp/', exist_ok=True)

# Save xmp file
file_path = './tmp/example.xmp'
with open(file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
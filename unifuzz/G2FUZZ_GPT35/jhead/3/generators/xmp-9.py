import os

# Create directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp file content
xmp_content = '''<?xpacket begin="�" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:LinkedData>https://example.com/linked_data</xmp:LinkedData>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Save xmp file
file_path = './tmp/linked_data.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file generated and saved at: {file_path}')
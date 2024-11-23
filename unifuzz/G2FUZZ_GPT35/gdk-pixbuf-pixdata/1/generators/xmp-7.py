import os

# Create the directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:StructuredData>
                <xmp:Feature>Efficient search and retrieval of information</xmp:Feature>
                <xmp:Feature>Structured metadata format</xmp:Feature>
            </xmp:StructuredData>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Save the XMP content to a file
file_path = os.path.join(directory, 'metadata.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file generated and saved at: {file_path}")
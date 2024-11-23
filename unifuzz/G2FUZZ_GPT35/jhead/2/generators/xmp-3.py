import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with the specified features
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Interoperability>XMP files are designed to be compatible with various file formats, allowing for the exchange of metadata across different applications and platforms.</xmp:Interoperability>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the generated XMP file
file_path = os.path.join(directory, 'sample.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file with the specified features generated and saved at: {file_path}")
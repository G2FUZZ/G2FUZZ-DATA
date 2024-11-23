import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file content
xmp_content = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Note>Embeddable: XMP metadata can be embedded within various file formats, such as images, videos, PDFs, and more, making it a versatile solution for metadata management.</xmp:Note>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save XMP file to tmp directory
file_path = os.path.join(directory, 'metadata.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file generated and saved at: {file_path}")
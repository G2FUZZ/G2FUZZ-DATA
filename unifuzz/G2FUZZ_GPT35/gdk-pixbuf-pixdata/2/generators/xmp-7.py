import os

# Define the content for the XMP file
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <xmp:CreatorTool>Python</xmp:CreatorTool>
            <xmp:Description>Interoperability: XMP files are designed to work seamlessly with Adobe products and other software that support the XMP standard.</xmp:Description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create a directory to store the XMP files if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the XMP file with the defined content
file_path = './tmp/interoperability.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
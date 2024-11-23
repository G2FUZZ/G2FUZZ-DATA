import os

# Define the content for the XMP file
xmp_content = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <xmp:CreateDate>2022-10-31T12:00:00</xmp:CreateDate>
            <dc:format>application/pdf</dc:format>
            <dc:description>Interoperability: XMP files are designed to be easily embedded within various file formats, making it interoperable across different applications and platforms.</dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Create a directory to store the XMP files if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Write the XMP content to a file
file_path = os.path.join(output_dir, 'interoperability.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file with the feature 'Interoperability' has been generated and saved at: {file_path}")
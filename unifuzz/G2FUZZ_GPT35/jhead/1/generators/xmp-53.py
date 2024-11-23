import os

# Define the content for the extended XMP file
xmp_content_extended = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:custom="http://example.com/custom/">
            <xmp:CreateDate>2022-10-31T12:00:00</xmp:CreateDate>
            <dc:format>application/pdf</dc:format>
            <dc:description>Interoperability: XMP files are designed to be easily embedded within various file formats, making it interoperable across different applications and platforms.</dc:description>
            <custom:customField1>Value 1</custom:customField1>
            <custom:customField2>Value 2</custom:customField2>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

# Create a directory to store the extended XMP files if it does not exist
output_dir_extended = './tmp/extended/'
os.makedirs(output_dir_extended, exist_ok=True)

# Write the extended XMP content to a file
file_path_extended = os.path.join(output_dir_extended, 'extended_interoperability.xmp')
with open(file_path_extended, 'w') as file:
    file.write(xmp_content_extended)

print(f"Extended XMP file with additional metadata fields has been generated and saved at: {file_path_extended}")
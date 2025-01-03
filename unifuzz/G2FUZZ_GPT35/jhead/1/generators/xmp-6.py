import os

# Define the XMP content
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <xmp:CreatorTool>Python</xmp:CreatorTool>
            <dc:format>application/pdf</dc:format>
            <xmp:CreateDate>2022-07-20T12:00:00</xmp:CreateDate>
            <xmp:ModifyDate>2022-07-20T13:00:00</xmp:ModifyDate>
            <dc:description>Structured Data: XMP allows for the representation of structured data through the use of schemas, properties, and qualifiers.</dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP content to a file
with open('./tmp/structured_data.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated successfully.")
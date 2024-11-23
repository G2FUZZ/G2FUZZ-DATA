import os

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:CreateDate>2022-10-12T14:22:16+00:00</xmp:CreateDate>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP file with the content
with open('./tmp/example.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated and saved successfully.")
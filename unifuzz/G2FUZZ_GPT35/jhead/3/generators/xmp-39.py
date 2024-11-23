import os

# Define the content for the XMP file with additional complex features
xmp_content_complex = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:custom="http://example.com/custom/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:title>XMP File with Complex Features</dc:title>
            <dc:creator>John Doe</dc:creator>
            <dc:date>2022-12-31</dc:date>
            <custom:customProperty>Custom Value</custom:customProperty>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the content to the XMP file with complex features
with open('./tmp/complex_xmp_file.xmp', 'w') as file:
    file.write(xmp_content_complex)

print("XMP file with complex features created at ./tmp/complex_xmp_file.xmp")
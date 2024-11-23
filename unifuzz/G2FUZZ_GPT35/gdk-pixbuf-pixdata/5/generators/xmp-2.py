import os

# Create a directory for storing generated xmp files
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the xmp file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:extensibility>XMP allows for custom schemas and properties to be defined and stored within the file.</custom:extensibility>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the xmp file
with open('./tmp/custom_xmp_file.xmp', 'w') as file:
    file.write(xmp_content)
import os

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:customProperty>Custom Value</custom:customProperty>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the tmp directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the XMP file in the tmp directory
with open('./tmp/custom_metadata.xmp', 'w') as file:
    file.write(xmp_content)
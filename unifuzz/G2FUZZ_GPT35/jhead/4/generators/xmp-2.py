import os

xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:custom="http://example.com/custom/"
            custom:extensibility="XMP allows for the creation of custom metadata schemas to suit specific needs."
        />
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

with open('./tmp/custom_metadata.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated successfully at ./tmp/custom_metadata.xmp")
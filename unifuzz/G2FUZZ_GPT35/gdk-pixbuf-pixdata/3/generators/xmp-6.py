import os

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="">
            <dc:language>
                <rdf:Bag>
                    <rdf:li>en</rdf:li>
                    <rdf:li>fr</rdf:li>
                    <rdf:li>es</rdf:li>
                </rdf:Bag>
            </dc:language>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP file with the specified content
with open('./tmp/multilingual_metadata.xmp', 'w') as f:
    f.write(xmp_content)
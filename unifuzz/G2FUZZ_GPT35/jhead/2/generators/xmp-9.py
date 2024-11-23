import os

# Define the XMP metadata content
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="">
            <xmp:Machine-readable>XMP metadata is designed to be machine-readable, enabling automated processing and extraction of metadata by software applications.</xmp:Machine-readable>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the XMP content to a file
with open('./tmp/metadata.xmp', 'w') as f:
    f.write(xmp_content)

print("XMP file generated successfully at ./tmp/metadata.xmp")
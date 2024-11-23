import os

# Define the content to be written in the xmp file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Preservation> XMP files can help in preserving important metadata associated with digital assets, aiding in their long-term archiving and retrieval. </xmp:Preservation>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the xmp file with the defined content
with open('./tmp/example.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated successfully.")
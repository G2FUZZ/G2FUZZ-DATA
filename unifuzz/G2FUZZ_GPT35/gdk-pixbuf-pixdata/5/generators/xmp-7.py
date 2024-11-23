import os

# Define the feature to be added to the XMP file
feature = "7. Language Support: XMP supports multiple languages for metadata descriptions and values."

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with the feature
with open('./tmp/example.xmp', 'w') as file:
    file.write(f'<?xpacket begin="\ufeff" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
    file.write(f'<x:xmpmeta xmlns:x="adobe:ns:meta/">\n')
    file.write(f'    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
    file.write(f'        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n')
    file.write(f'            <xmp:CustomProperty>\n')
    file.write(f'                <xmp:PropertyName>Feature</xmp:PropertyName>\n')
    file.write(f'                <xmp:Value>{feature}</xmp:Value>\n')
    file.write(f'            </xmp:CustomProperty>\n')
    file.write(f'        </rdf:Description>\n')
    file.write(f'    </rdf:RDF>\n')
    file.write(f'</x:xmpmeta>\n')
    file.write(f'<?xpacket end="w"?>\n')

print("XMP file generated and saved as './tmp/example.xmp'")
import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with embedded thumbnails
for i in range(3):
    filename = f'{directory}file_{i}.xmp'
    with open(filename, 'w') as file:
        file.write(f'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
        file.write(f'<x:xmpmeta xmlns:x="adobe:ns:meta/">\n')
        file.write(f'<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
        file.write(f'<rdf:Description rdf:about=""\n')
        file.write(f'xmlns:dc="http://purl.org/dc/elements/1.1/">\n')
        file.write(f'<dc:format>image/jpeg</dc:format>\n')
        file.write(f'</rdf:Description>\n')
        file.write(f'<rdf:Description rdf:about=""\n')
        file.write(f'xmlns:xap="http://ns.adobe.com/xap/1.0/">\n')
        file.write(f'<xap:Thumbnails>\n')
        file.write(f'<rdf:Alt>\n')
        file.write(f'<rdf:li rdf:parseType="Resource">\n')
        file.write(f'<rdf:Description rdf:about=""\n')
        file.write(f'xmlns:stDim="http://ns.adobe.com/xap/1.0/sType/Dimensions#">\n')
        file.write(f'<stDim:w>100</stDim:w>\n')
        file.write(f'<stDim:h>100</stDim:h>\n')
        file.write(f'</rdf:Description>\n')
        file.write(f'</rdf:li>\n')
        file.write(f'</rdf:Alt>\n')
        file.write(f'</xap:Thumbnails>\n')
        file.write(f'</rdf:Description>\n')
        file.write(f'</rdf:RDF>\n')
        file.write(f'</x:xmpmeta>\n')
        file.write(f'<?xpacket end="w"?>\n')

    print(f'Generated XMP file: {filename}')
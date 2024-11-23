import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with versioning information
for i in range(1, 6):
    filename = f'{directory}file{i}.xmp'
    with open(filename, 'w') as file:
        file.write(f'<?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
        file.write(f'<x:xmpmeta xmlns:x="adobe:ns:meta/">\n')
        file.write(f'    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
        file.write(f'        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n')
        file.write(f'            <xmp:Version>{i}.0</xmp:Version>\n')
        file.write(f'        </rdf:Description>\n')
        file.write(f'    </rdf:RDF>\n')
        file.write(f'</x:xmpmeta>\n')
        file.write(f'<?xpacket end="w"?>\n')

    print(f'Generated {filename}')

print('XMP files generated successfully!')
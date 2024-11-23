import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP files
for i in range(1, 4):
    filename = f'./tmp/file{i}.xmp'
    with open(filename, 'w') as file:
        file.write('<?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?>\n')
        file.write('<x:xmpmeta xmlns:x="adobe:ns:meta/">\n')
        file.write('  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
        file.write('    <rdf:Description rdf:about=""\n')
        file.write('      xmlns:custom="http://example.com/custom/">\n')
        file.write('      <custom:extensibility>XMP files support custom schemas and properties, allowing users to define and include their own metadata fields.</custom:extensibility>\n')
        file.write('    </rdf:Description>\n')
        file.write('  </rdf:RDF>\n')
        file.write('</x:xmpmeta>\n')
        file.write('<?xpacket end="w"?>\n')

print('XMP files generated and saved in ./tmp/')
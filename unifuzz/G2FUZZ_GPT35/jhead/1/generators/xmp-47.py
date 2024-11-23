import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with complex file structures
num_files = 5

for i in range(num_files):
    with open(f'./tmp/file_{i}.xmp', 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159661, 2018/09/12-16:52:51">\n')
        file.write('\t<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n')
        file.write('\t\t<rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n')
        file.write('\t\t\t<xmp:CreatorTool>MyXMPTool</xmp:CreatorTool>\n')
        file.write('\t\t</rdf:Description>\n')
        file.write('\t</rdf:RDF>\n')
        file.write('</x:xmpmeta>')

print(f'{num_files} xmp files with complex file structures generated and saved in ./tmp/')
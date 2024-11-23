import os

# Create a directory to save xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with hierarchical structure
for i in range(3):
    filename = f'./tmp/file_{i}.xmp'
    with open(filename, 'w') as f:
        f.write(f'<x:xmpmeta xmlns:x="adobe:ns:meta/">{os.linesep}')
        f.write(f'    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">{os.linesep}')
        f.write(f'        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">{os.linesep}')
        f.write(f'            <xmp:HierarchicalStructure>{i}</xmp:HierarchicalStructure>{os.linesep}')
        f.write(f'        </rdf:Description>{os.linesep}')
        f.write(f'    </rdf:RDF>{os.linesep}')
        f.write(f'</x:xmpmeta>{os.linesep}')

print('XMP files generated successfully!')
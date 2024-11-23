import os

# Create a directory to store the generated xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with more complex file structures
for i in range(3):
    filename = f'./tmp/file_{i}.xmp'
    with open(filename, 'w') as f:
        f.write(
            f'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
            f'<x:xmpmeta xmlns:x="adobe:ns:meta/">\n'
            f'  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
            f'    <rdf:Description rdf:about="file_{i}.jpg" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n'
            f'      <xmp:HierarchicalStructure>Complex relationships and dependencies</xmp:HierarchicalStructure>\n'
            f'      <xmp:CustomTag1>Custom Value 1</xmp:CustomTag1>\n'
            f'      <xmp:CustomTag2>Custom Value 2</xmp:CustomTag2>\n'
            f'      <xmp:Layer1>\n'
            f'        <xmp:SubLayer1>Sublayer Value 1</xmp:SubLayer1>\n'
            f'        <xmp:SubLayer2>Sublayer Value 2</xmp:SubLayer2>\n'
            f'      </xmp:Layer1>\n'
            f'      <xmp:Layer2>\n'
            f'        <xmp:SubLayer3>Sublayer Value 3</xmp:SubLayer3>\n'
            f'        <xmp:SubLayer4>Sublayer Value 4</xmp:SubLayer4>\n'
            f'      </xmp:Layer2>\n'
            f'    </rdf:Description>\n'
            f'  </rdf:RDF>\n'
            f'</x:xmpmeta>\n'
            f'<?xpacket end="w"?>'
        )
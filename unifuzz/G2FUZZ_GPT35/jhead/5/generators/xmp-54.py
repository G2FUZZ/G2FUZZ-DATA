import os

# Create a directory to store the generated xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with complex features
for i in range(3):
    filename = f'./tmp/file_{i}.xmp'
    with open(filename, 'w') as f:
        f.write(
            f'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
            f'<x:xmpmeta xmlns:x="adobe:ns:meta/">\n'
            f'  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
            f'    <rdf:Description rdf:about="file_{i}.jpg" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n'
            f'      <xmp:HierarchicalStructure>Complex relationships and dependencies</xmp:HierarchicalStructure>\n'
            f'      <xmp:CustomProperty1>Custom Value 1</xmp:CustomProperty1>\n'
            f'      <xmp:CustomProperty2>Custom Value 2</xmp:CustomProperty2>\n'
            f'      <xmp:NestedStructure>\n'
            f'        <xmp:SubProperty1>Sub Value 1</xmp:SubProperty1>\n'
            f'        <xmp:SubProperty2>Sub Value 2</xmp:SubProperty2>\n'
            f'      </xmp:NestedStructure>\n'
            f'    </rdf:Description>\n'
            f'  </rdf:RDF>\n'
            f'</x:xmpmeta>\n'
            f'<?xpacket end="w"?>'
        )
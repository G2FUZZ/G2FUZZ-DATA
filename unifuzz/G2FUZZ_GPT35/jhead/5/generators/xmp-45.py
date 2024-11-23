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
            f'      <xmp:CustomMetadata>\n'
            f'        <xmp:CustomField1>Value1</xmp:CustomField1>\n'
            f'        <xmp:CustomField2>Value2</xmp:CustomField2>\n'
            f'      </xmp:CustomMetadata>\n'
            f'      <xmp:RelatedFiles>\n'
            f'        <rdf:Seq>\n'
            f'          <rdf:li>file_{i}_related1.jpg</rdf:li>\n'
            f'          <rdf:li>file_{i}_related2.jpg</rdf:li>\n'
            f'        </rdf:Seq>\n'
            f'      </xmp:RelatedFiles>\n'
            f'    </rdf:Description>\n'
            f'  </rdf:RDF>\n'
            f'</x:xmpmeta>\n'
            f'<?xpacket end="w"?>'
        )
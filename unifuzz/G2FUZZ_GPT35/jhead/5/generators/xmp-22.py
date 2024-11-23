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
            f'      <xmp:Rating>5</xmp:Rating>\n'
            f'      <xmp:Tags>\n'
            f'        <rdf:Bag>\n'
            f'          <rdf:li>Tag1</rdf:li>\n'
            f'          <rdf:li>Tag2</rdf:li>\n'
            f'        </rdf:Bag>\n'
            f'      </xmp:Tags>\n'
            f'      <xmp:CustomField>\n'
            f'        <xmp:Field1>Value1</xmp:Field1>\n'
            f'        <xmp:Field2>Value2</xmp:Field2>\n'
            f'      </xmp:CustomField>\n'
            f'    </rdf:Description>\n'
            f'  </rdf:RDF>\n'
            f'</x:xmpmeta>\n'
            f'<?xpacket end="w"?>'
        )
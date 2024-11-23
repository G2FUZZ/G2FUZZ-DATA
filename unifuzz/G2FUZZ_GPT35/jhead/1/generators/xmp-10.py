import os

metadata = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:dc="http://purl.org/dc/elements/1.1/">
    <xmp:Accessibility>
      <rdf:Seq>
        <rdf:li>10. Accessibility: XMP metadata can improve the accessibility of files by providing descriptive information that can be used by assistive technologies.</rdf:li>
      </rdf:Seq>
    </xmp:Accessibility>
  </rdf:Description>
</rdf:RDF>
"""

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

for i in range(3):
    with open(f'./tmp/file_{i}.xmp', 'w') as f:
        f.write(metadata)

print("XMP files generated successfully in ./tmp/")
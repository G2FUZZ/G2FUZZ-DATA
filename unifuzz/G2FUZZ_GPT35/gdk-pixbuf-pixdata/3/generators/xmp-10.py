import os

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c067 79.157747, 2015/03/30-23:40:42        ">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/"
        xmlns:dc="http://purl.org/dc/elements/1.1/">
      <xmp:ModifyDate>2018-09-12T16:13:03+02:00</xmp:ModifyDate>
      <xmp:MetadataDate>2018-09-12T16:13:03+02:00</xmp:MetadataDate>
      <dc:format>image/png</dc:format>
      <dc:creator>
        <rdf:Seq>
          <rdf:li>John Doe</rdf:li>
        </rdf:Seq>
      </dc:creator>
      <dc:title>
        <rdf:Alt>
          <rdf:li xml:lang="x-default">Sample Image</rdf:li>
        </rdf:Alt>
      </dc:title>
      <dc:description>
        <rdf:Alt>
          <rdf:li xml:lang="x-default">This is a sample image.</rdf:li>
        </rdf:Alt>
      </dc:description>
      <dc:subject>
        <rdf:Bag>
          <rdf:li>Metadata</rdf:li>
          <rdf:li>XMP</rdf:li>
          <rdf:li>Versioning</rdf:li>
        </rdf:Bag>
      </dc:subject>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP file with the defined content
file_path = './tmp/sample.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
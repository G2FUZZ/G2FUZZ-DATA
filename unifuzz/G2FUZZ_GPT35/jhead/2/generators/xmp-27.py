import os

# Define the metadata content with more complex file features
metadata_content = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:custom="http://example.com/custom/namespace#">
  <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
    <xmp:Title>Title of the Document</xmp:Title>
    <xmp:Creator>John Doe</xmp:Creator>
    <xmp:CreateDate>2022-01-01</xmp:CreateDate>
    <xmp:Description>This is a sample XMP file with complex features.</xmp:Description>
    <xmp:Language>en-US</xmp:Language>
  </rdf:Description>
  <rdf:Description rdf:about="resource1.pdf">
    <custom:CustomProperty1>Value 1</custom:CustomProperty1>
    <custom:CustomProperty2>Value 2</custom:CustomProperty2>
  </rdf:Description>
  <rdf:Description rdf:about="resource2.jpg">
    <custom:CustomProperty3>Value 3</custom:CustomProperty3>
  </rdf:Description>
</rdf:RDF>
"""

# Create a directory to store XMP files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the metadata content to a new XMP file with complex features
file_path = './tmp/sample_complex_metadata.xmp'
with open(file_path, 'w') as f:
    f.write(metadata_content)

print(f"XMP file with complex features generated and saved at: {file_path}")
import os

# Define the metadata content
metadata_content = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
    <xmp:Title>Title of the Document</xmp:Title>
    <xmp:Creator>John Doe</xmp:Creator>
    <xmp:CreateDate>2022-01-01</xmp:CreateDate>
    <xmp:Description>This is a sample XMP file for demonstration purposes.</xmp:Description>
    <xmp:Language>en-US</xmp:Language>
  </rdf:Description>
</rdf:RDF>
"""

# Create a directory to store XMP files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the metadata content to a new XMP file
file_path = './tmp/sample_metadata.xmp'
with open(file_path, 'w') as f:
    f.write(metadata_content)

print(f"XMP file generated and saved at: {file_path}")
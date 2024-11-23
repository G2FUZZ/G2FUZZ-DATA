import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# XMP content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <xmp:CreatorTool>Custom Python Script</xmp:CreatorTool>
   <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
   <xmp:MetadataDate>2023-01-01T12:00:00</xmp:MetadataDate>
   <xmp:ModifyDate>2023-01-01T12:00:00</xmp:ModifyDate>
   <xmp:Label>Interoperability</xmp:Label>
   <xmp:Description>Interoperability: XMP provides a standard format for metadata across different file types, making it easier to transfer information between different applications and services without losing metadata. This is crucial for workflows in photography, design, and digital asset management.</xmp:Description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Save the XMP content into a file
file_path = './tmp/features.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file saved at: {file_path}')
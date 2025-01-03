import os

# Ensuring the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# XMP content with the feature "Synchronization"
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <xmp:CreatorTool>Example Tool</xmp:CreatorTool>
   <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
   <xmp:MetadataDate>2023-01-01T12:00:00</xmp:MetadataDate>
   <xmp:ModifyDate>2023-01-01T12:00:00</xmp:ModifyDate>
   <xmp:Label>Synchronization</xmp:Label>
   <xmp:Description>Synchronization: XMP allows for the synchronization of metadata across different files, ensuring consistency in information across multiple file formats and systems.</xmp:Description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# File path for the XMP file
file_path = os.path.join(output_dir, 'feature_synchronization.xmp')

# Writing the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file created at {file_path}')
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>4. **Embeddable**: Can be embedded directly into the file it describes (such as JPEG or PDF), or exist as a sidecar file alongside formats that do not support direct embedding, ensuring metadata is kept with the file.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Define the path for the new XMP file
xmp_file_path = './tmp/description_metadata.xmp'

# Write the content to the XMP file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f'XMP file saved to {xmp_file_path}')
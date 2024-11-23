import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    3. **Embeddability**: XMP data can be embedded directly into digital files including JPEG, TIFF, PDF, and many RAW formats, among others. This ensures that the metadata travels with the file, providing contextual information wherever the file goes.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Define the file path
file_path = './tmp/feature_description.xmp'

# Write the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file has been saved to {file_path}')
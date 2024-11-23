import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>3. **Embeddability**: XMP can be embedded into the file it describes, such as JPEG, PDF, TIFF, MP4, and many others, allowing the metadata to travel with the file wherever it goes.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Path to the XMP file
xmp_file_path = './tmp/feature_description.xmp'

# Write the content to the XMP file
with open(xmp_file_path, 'w') as file:
    file.write(xmp_content)
    
print(f"XMP file created at: {xmp_file_path}")